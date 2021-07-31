import requests
from lxml import etree
import os
from bs4 import BeautifulSoup
import csv

#header = ['排名','片名','评分','评价人数','年份','地区','时长']
# fp =open('test2.csv','a',newline='')
# f_csv = csv.DictWriter(fp,header)
# f_csv.writeheader()
if __name__ == '__main__':
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	header = ['排名','片名','评分','评价人数','年份','地区','时长']
	url = 'https://movie.douban.com/top250?start=%d'

	for pageNum in range(0,251,25):
		#获取每个分页的url
		new_url = format(url%pageNum)
		print(new_url)
		# page_text = requests.get(url=new_url,headers=headers).text

		# tree = etree.HTML(page_text)
		# url_list = tree.xpath('//div[@class="hd"]/a/@href')
		# # title_list = tree.xpath('//div[@class="item"]/div/a/img/@alt')
		# # for i in range(0,len(title_list)):
		# # 	#print(title_list[i])
		# # 	Title.setdefault('片名',[]).append(title_list[i])
		# # 	print(Title{0})
		# # print(url_list)
		# fp =open('test2.csv','a',newline='')
		# f_csv = csv.DictWriter(fp,header)
		# #f_csv.writeheader()
		# for nurl in url_list:
		# 	#print(nurl)
		# 	detail_text = requests.get(url=nurl,headers=headers).content.decode('utf-8')

		# 	ntree = etree.HTML(detail_text)
		# 	# 爬取电影的排名
		# 	# No_list = ntree.xpath('//div[@class="top250"]/span/text()')
		# 	# for no in No_list:
		# 	# 	list1 = ['排名']
		# 	# 	Number = [dict(zip(list1,No_list))]
		# 	# 	# with open('test.csv','a',newline='') as f:
		# 	# 	# 	f_csv = csv.DictWriter(f,header)
		# 	# 	# 	f_csv.writeheader()
		# 	# 	f_csv.writerows(Number)
		# 	# 	#print(Number)
		# 	# 	print('worked')


		# 	# #print(No_list)
		# 	#爬取电影名
		# 	Title_list = ntree.xpath('//div[@class="subject clearfix"]/div/a/img/@alt')
		# 	# print(Name_list)
			
		# 	for ti in Title_list:
		# 		#print(ti)
		# 		list2 = ['片名']
		# 		Title = [dict(zip(list2,Title_list))]
		# 		f_csv.writerows(Title)
		# 		print('Title_list,worked')
				#print(Title)
			# 爬取电影评分
			# Score_list = ntree.xpath('//div[@class="rating_self clearfix"]/strong/text()')
			# for sc in Score_list:
			# 	list3 = ['评分']
			# 	Score = dict(zip(list3,Score_list))
				#print(Score)
			# 爬取电影评价人数
			# Rate_list = ntree.xpath('//div[@class="rating_sum"]/a/span/text()')
			# for ra in Rate_list:
			# 	list4 = ['评价人数']
			# 	Rate = dict(zip(list4,Rate_list))
			# 	#print(Rate)
			# 爬取电影年份
			# Year_list = ntree.xpath('//div[@id="content"]/h1/span[@class="year"]/text()')
			# for ye in Year_list:
			# 	list5 = ['年份']
			# 	Year = dict(zip(list5,Year_list))
			# 	#print(Year)
			# 爬取电影上映地区
			# City_list = ntree.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"][1]/@content')
			# for ci in City_list:
			# 	# print(dr)
			# 	list6= ['地区']
			# 	City = dict(zip(list6,City_list))
				# print(City)
			# Lenth_list = ntree.xpath('//div[@id="info"]/span[@property="v:runtime"]/@content')
			# for le in Lenth_list:
			# 	#print(le)
			# 	list7 = ['时长']
			# 	Lenth = dict(zip(list7,Lenth_list))
			# 	print(Lenth)

