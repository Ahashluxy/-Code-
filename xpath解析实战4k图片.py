import requests
from lxml import etree
import os

if __name__ == '__main__':
	url = 'https://pic.netbian.com/4kmeinv/index_3.html'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	response = requests.get(url=url,headers=headers)
	#response.encoding = 'utf-8'
	page_text = response.text
	tree = etree.HTML(page_text)

	#解析src的属性值，alt的属性值
	li_list = tree.xpath('//div[@class="slist"]//li')
	# print(li_list)

	# 创建一个文件夹
	# if not os.path.exists('./picLibs'):
	# 	os.mkdir('./picLibs')
	# for li in li_list:
	# 	img_src = 'https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
	# 	img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
	# 	# 通用的解决中文乱码的问题
	# 	img_name = img_name.encode('iso-8859-1').decode('gbk')
	# 	# print(img_name,img_src)
	# 	# 请求图片进行持久化存储
	# 	img_data = requests.get(url=img_src,headers=headers).content
	# 	img_path = 'picLibs/'+img_name
	# 	with open(img_path,'wb') as fp:
	# 		fp.write(img_data)
	# 		print(img_name,'下载成功!!!')
