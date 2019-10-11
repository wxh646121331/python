# coding:utf-8
import requests
import json
from selenium import webdriver

query = '王祖贤'
''' 下载图片 '''
def download(src, id):
	dir = './images/' + str(id) + '.jpg'
	try:
		pic = requests.get(src, timeout=10)
		fp = open(dir, 'wb')
		fp.write(pic.content)
		fp.close()
	except requests.exceptions.ConnectionError:
		print('图片无法下载')
            
''' for 循环 请求全部的 url '''
for i in range(0, 20, 20):
	url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)
	html = requests.get(url).text    # 得到返回结果
	response = json.loads(html,encoding='utf-8') # 将 JSON 格式转换成 Python 对象
	for image in response['images']:
		print(image['src']) # 查看当前下载的图片网址
		#download(image['src'], image['id']) # 下载一张图片




driver = webdriver.Chrome('/Users/wuxinhong/myapps/chromedriver')
request_url = 'https://movie.douban.com/subject_search?search_text='+query+'&cat=1002';
result = driver.get(request_url)
print(result)
