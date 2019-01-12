import requests
import jsonpath
import json
import chardet

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; \
.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"}

response = requests.get(url, headers=headers)
html = response.content.decode()

# 把json格式字符串转换成python对象
jsonobj = json.loads(html)

citylist = jsonpath.jsonpath(jsonobj, "$..name")

print(citylist)

fp = open("city.json", "w")

# 把python对象转换为json字符串
content = json.dumps(citylist, ensure_ascii=False)

print(content)

fp.write(content)

fp.close()





print(jsonobj)

print(html)
