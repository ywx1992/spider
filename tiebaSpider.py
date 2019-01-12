import requests


class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        self.url = "https://tieba.baidu.com/f?kw={}&pn={}"

    def load_page(self, url):  # 发送请求，获取相应
        # print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_page(self, html, page_num):  # 保存html字符串
        file_name = "{}吧第{}页.html".format(self.tieba_name, page_num)
        with open(file_name, "w") as f:
            f.write(html)

    def run(self):  # 实现主要逻辑
        url_list = [self.url.format(self.tieba_name, i * 50) for i in range(1000)]  # 构造url列表
        for url in url_list:
            html = self.load_page(url)
            page_num = url_list.index(url) + 1
            self.save_page(html, page_num)


if __name__ == "__main__":
    tiba_name = input("请输入贴吧名:")
    t = TiebaSpider(tiba_name)
    t.run()
