from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 将本地的html加载到该对象当中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.a) # soup.tagName返回的html中第一次出现的tagName的标签
    # print(soup.div)
    # print(soup.find('div'))
    # 注意class_的下划线
    # print(soup.find('div', class_='song'))
    # print(soup.find_all('a'))  # 返回符合要求的所有标签以列表的形式
    print(soup.select('.tang> ul a')[0]['href'])
