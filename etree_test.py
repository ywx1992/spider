from lxml import etree
import requests
import chardet

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"
}

response = requests.get("https://tieba.baidu.com/f?kw=lol&pn=0", headers=headers)
html_str = response.content.decode()
# print(html)

# 将html字符串解析为html文档
selector = etree.HTML(html_str)
print(selector)
links = selector.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')

print(links)
print(chardet.detect(b'Hello, world!'))
