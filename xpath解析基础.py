import requests
from lxml import html

etree = html.etree

if __name__ == '__main__':
    # 实例化好了一个etree对象，并将被解析的源码加载到了该对象中
    tree = etree.parse('test.html')
    # r = tree.xpath('/html/body/div')# 返回的都是列表
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="song"]')
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]
    # r = tree.xpath('//li[7]/i/text()')[0]
    # r = tree.xpath('//div[@class="tang"]//text()')
    r = tree.xpath('//div[@class="song"]/img/@src')

    print(r)
