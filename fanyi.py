import requests
import json
import sys
import re


url = "http://m.youdao.com/translate"

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"}

trans = input("翻译：")

data = {
    # "inputtext": sys.argv[1],
    "inputtext": trans,
    "type": "AUTO"
}

response = requests.post(url, data=data, headers=headers)

# print(response.content.decode())


res = re.findall(r'<ul.*?id="translateResult">\s*<li>(.*?)</li>', response.content.decode(), re.S)[0]

print("结果:", res)
