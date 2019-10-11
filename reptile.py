import requests
from lxml import etree, html
import lxml
import json



# get请求
r = requests.get('http://www.douban.com')
# print(r)
# print(r.text)
#print(r.content)

# post请求
# r = requests.post('http://xxx.com', data = {'key':'value'})


print('-'*35+'xml'+'-'*35)
html = etree.HTML(r.content)
result = html.xpath('//li')
print(result)


print('-'*35+'json'+'-'*35)
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
# json.loads:将json对象转换成python对象
input = json.loads(jsonData)
print(input)
print(type(input))
# json.dumps:将python对象转换成json对象
jsonData = json.dumps(input)
print(jsonData)
print(type(jsonData))


