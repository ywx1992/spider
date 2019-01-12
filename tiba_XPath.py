import requests
from lxml import etree


class TiebaSpider(object):
    def __init__(self, tiebaName, startPage, endPage):
        self.tiebaName = tiebaName
        self.startPage = startPage
        self.endPage = endPage

        self.url = "https://tieba.baidu.com/f?"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"}

    def load_page(self, url):
        response = requests.get(url, headers=self.headers)
        html = response.content.decode()
        # print(html)

        # 将html字符串解析为html文档
        selector = etree.HTML(html)
        links = selector.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        print(links)
        for link in links[:-1]:
            # 每个帖子的完整链接
            link = "http://tieba.baidu.com/" + link
            print(link)
            self.load_image(link)

    def load_image(self, link):
        print("正在下载图片")
        response = requests.get(link, headers=self.headers)
        html = response.content.decode()
        html = etree.HTML(html)

        image_links = html.xpath('//img[@class="BDE_Image"]/@src')

        for image_link in image_links:
            self.save_image(image_link)

    def save_image(self, image_link):
        print("正在保存文件")
        response = requests.get(image_link, headers=self.headers)
        image = response.content
        filename = image_link[-10:]
        with open("./images/" + filename, "wb") as f:
            f.write(image)
        print("保存图片成功" + filename)

    def run(self):
        for page in range(self.startPage, self.endPage + 1):
            full_url = self.url + "kw={}&pn={}".format(self.tiebaName, (page - 1) * 50)
            self.load_page(full_url)


if __name__ == "__main__":
    spider = TiebaSpider("", 2, 2)
    spider.run()
