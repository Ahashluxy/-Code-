#coding=utf-8
import re
import requests
from lxml import etree
import os
from bs4 import BeautifulSoup
import csv

with open('test3.csv', 'a',encoding='utf-8-sig',newline='') as f:

    writer = csv.writer(f, dialect='excel')
    writer.writerow(['电影排名', '电影名称', '评分', '短评', '评价人数', '导演','电影海报'])
def get_page_url(pageNum):


	url = 'https://movie.douban.com/top250?start=%d'

	#for pageNum in range(0,251,25):
		#获取每个分页的url
	new_url = format(url%pageNum)
	# print(new_url)
	return new_url

def get_detail_url(nurl):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	page_text = requests.get(url=nurl,headers=headers).text
	tree = etree.HTML(page_text)
	detail_url_list = tree.xpath('//div[@class="hd"]/a/@href')
	return detail_url_list
def get_page(nurl):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	page_text = requests.get(url=nurl,headers=headers).text
	return page_text

def parseHtml(page_text,nurl):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	response = requests.get(url=nurl,headers=headers).content.decode('utf-8')
	tree = etree.HTML(page_text)
	Title = tree.xpath('//div[@class="hd"]//a//span[1]//text()')
	Score = tree.xpath('//div[@class="star"]//span[2]//text()')
	Rank = tree.xpath('//div[@class="item"]//div//em//text()')
	Info = tree.xpath('//div[@class="bd"]/p[@class="quote"]/span/text()')
	Rate = tree.xpath('//div[@class="star"]/span[4]/text()')
	Director = re.findall(r"导演:(.*?);", response)
	a = "".join(Director).split("&nbsp")#因为使用的正则抓取下来的字符串含有&nbsp，使用split()函数进行切分
	Director = a[:25]
	Poster = tree.xpath('//div[@class="pic"]/a/img/@src')
	for q,w,e,r,t,y,u in list(zip(Rank,Title,Score,Info,Rate,Director,Poster)):
		print(q,w,e,r,t,y,u)
		with open('test3.csv','a',encoding='utf-8-sig',newline='') as f:
			writer = csv.writer(f, dialect='excel')
			writer.writerow([q,w,e,r,t,y,u])

if __name__ == '__main__':
	for i in range(0,226,25):
		nurl = get_page_url(i)
		page_text = get_page(nurl)
		parseHtml(page_text,nurl)
		#print(nurl)
		# detail_list = get_detail_url(nurl)
		# print(detail_list)
		# for detail in detail_list:
		# 	parseHtml(detail)
	#nurl = get_detail_url()
	
	#main()
	