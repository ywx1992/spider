import requests
from PIL import Image
from io import StringIO, BytesIO

kw = {'wd': '联通'}

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)

#返回响应内容，字节流数据
print(response.content)
#完整url地址
print(response.url)
#响应头部字符编码
print(response.encoding)
#响应状态码
print(response.status_code)

print(response.request.headers)

img_url = "http://c.hiphotos.baidu.com/image/pic/item/0eb30f2442a7d933b29eb303a04bd11373f0018f.jpg"

response = requests.get(img_url)

f = BytesIO(response.content)

img = Image.open(f)

print(img.size)