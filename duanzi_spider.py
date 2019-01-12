import requests
import re


class Spider(object):
    def __init__(self):
        self.page = 1
        self.switch = True

    def load_page(self):
        """
        下载页面
        """
        url = "http://www.budejie.com/" + str(self.page)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        html = response.content.decode()
        # 创建正则表达式，匹配每页的段子内容
        pattern = re.compile(r'<div\sclass="j-r-list-c-desc">\s*<a\shref="/detail-\d+\.html">(.*?)</a>', re.S)
        # 段子列表
        content_list = pattern.findall(html)
        self.save_content(content_list)

    def save_content(self, content_list):
        """
        保存到本地文件
        content_list:
        """
        for content in content_list:
            content = content.replace("&quot;", "\"").replace("<br />", "") + "\n"
            with open("duanzi.txt", "a") as f:
                f.write(content)

    def start_work(self):
        """
        控制爬虫工作
        """
        while self.switch:
            self.load_page()
            self.page += 1
            if self.page > 50:
                self.switch = False


if __name__ == "__main__":
    spider = Spider()
    spider.start_work()
