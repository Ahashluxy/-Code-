import requests
from lxml import etree
import os

if __name__ == '__main__':
	url = 'https://sc.chinaz.com/jianli/fengmian.html'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	page_text = requests.get(url=url,headers=headers).content.decode('utf-8')
	#print(page_text)

	tree = etree.HTML(page_text)

	div_list = tree.xpath('//div[@class="box col3 ws_block"]')
	# print(div_list)
	if not os.path.exists('./jianli'):
		os.mkdir('./jianli')
	for div in div_list:
		img_src = 'https:'+div.xpath('./a/img/@src')[0]
		# print(img_src)
		img_name = div.xpath('./a/img/@alt')[0]+'.jpg'
		#print(img_name,img_src)
		img_data = requests.get(url=img_src,headers=headers).content
		img_path = 'jianli/'+img_name
		with open(img_path,'wb') as fp:
			fp.write(img_data)
			print(img_name,'下载成功！')