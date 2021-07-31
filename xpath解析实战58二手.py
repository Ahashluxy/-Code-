import requests
from lxml import html

etree = html.etree
# 爬取58二手房的房源信息
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    # 首先爬取页面的源码数据
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    # div_list = tree.xpath('//section[@class="list"]/div')
    # for div in div_list:
        # div.xpath('')
    h3_list = tree.xpath('//div[@class="property-content-title"]/h3/@title')
    print(h3_list)
    fp = open('58title.txt', 'w', encoding='utf-8')
    # fp.writelines(h3_list)
    for li in h3_list:
        fp.write(li+'\n')

