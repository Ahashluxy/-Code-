import requests
from lxml import etree

if __name__ == '__main__':
	# url = 'https://www.aqistudy.cn/historydata/'
	# headers = {
	# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	# }
	# page_text = requests.get(url=url,headers=headers).text

	# tree = etree.HTML(page_text)
	# hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
	# all_city_names = []
	# # 解析的是热门城市的名称
	# for li in hot_li_list:
	# 	hot_city_name = li.xpath('./a/text()')[0]
	# 	all_city_names.append(hot_city_name)
	# city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
	# # 解析的是全部城市的名称
	# for li in city_names_list:
	# 	city_name = li.xpath('./a/text()')[0]
	# 	all_city_names.append(city_name)

	# print(all_city_names,len(all_city_names))
	url = 'https://www.aqistudy.cn/historydata/'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
	}
	page_text = requests.get(url=url,headers=headers).text

	tree = etree.HTML(page_text)
	a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
	all_city_names = []
	fp=open('./citys.txt','w',encoding='utf-8')
	for a in a_list:
		city_name = a.xpath('./text()')[0]
		all_city_names.append(city_name)
		fp.write(city_name+'\n\t')

	print(all_city_names,len(all_city_names))
	