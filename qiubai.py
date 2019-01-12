import requests
from lxml import etree
import json


class QiubaiSpider(object):
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; \
            .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath(".//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            # 头像
            avatar = div.xpath("./div/a/img/@src")
            item["avatar"] = "https:" + avatar[0] if len(avatar) > 0 else None  # 匿名用户无头像、性别、年龄
            # 姓名
            item["name"] = div.xpath(".//h2/text()")[0].replace("\n", "")
            # 性别
            gender = div.xpath(".//div[contains(@class, 'articleGender')]/@class")
            item["gender"] = gender[0].split(" ")[1].replace("Icon", "") if len(gender) > 0 else None
            # 年龄
            age = div.xpath(".//div[contains(@class, 'articleGender')]/text()")
            item["age"] = age[0] if len(age) > 0 else None
            # 正文内容
            content = div.xpath(".//div[@class ='content']/span/text()")
            item["content"] = [i.replace("\n", "") for i in content][0]
            # 点赞数
            item["vote_number"] = div.xpath(".//span[1]/i/text()")[0]
            # 评论数
            item["comment_number"] = div.xpath(".//span[2]/a/i/text()")[0]

            content_list.append(item)
        return content_list

    def save_content(self, content_list):
        with open("qiubai.json", "a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')

    def run(self):  # 实现主要逻辑
        url_list = [self.url_temp.format(i) for i in range(1, 14)]  # 总共13页
        for url in url_list:
            html_str = self.parse_url(url)
            content_list = self.get_content(html_str)
            self.save_content(content_list)
            print("保存成功！")


if __name__ == "__main__":
    qs = QiubaiSpider()
    qs.run()
