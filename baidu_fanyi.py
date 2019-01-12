import requests
import json


class BaiduFanyi(object):
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.langdetect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 \
            (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content.decode())

    def run(self):
        # 获取语言类型
        langdetect_data = {"query": self.trans_str}
        lang = self.parse_url(self.langdetect_url, langdetect_data)["lan"]
        # 准备post数据
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else \
            {"query": self.trans_str, "from": "en", "to": "zh"}
        # 发送请求，获取响应，提取翻译结果
        dict_response = self.parse_url(self.trans_url, trans_data)
        result = dict_response["trans"][0]["dst"]
        print("翻译结果：", result)


if __name__ == "__main__":
    trans_str = input("请输入需要翻译的内容:")
    bf = BaiduFanyi(trans_str)
    bf.run()
