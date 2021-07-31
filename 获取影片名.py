import requests
from lxml import etree
import os
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	url = 'https://movie.douban.com/top250?start=%d'
	
	for pageNum in range(0,251,25):
		#获取每个分页的url
		new_url = format(url%pageNum)
		# print(new_url)
		page_text = requests.get(url=new_url,headers=headers).text

		tree = etree.HTML(page_text)
		url_list = tree.xpath('//div[@class="hd"]/a/@href')
		# title_list = tree.xpath('//div[@class="item"]/div/a/img/@alt')
		# for i in range(0,len(title_list)):
		# 	#print(title_list[i])
		# 	Title.setdefault('片名',[]).append(title_list[i])
		# 	print(Title{0})
		# print(url_list)
		for nurl in url_list:
			#print(nurl)
			detail_text = requests.get(url=nurl,headers=headers).text

			ntree = etree.HTML(detail_text)
			title_list = tree.xpath('//div[@id="content"]/h1/span[@class="year"]/text()')
			for ti in title_list:

				print(ti)