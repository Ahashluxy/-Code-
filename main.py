# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

if __name__ == '__main__':
    # 1 指定url
    url = 'https://www.sogou.com/'
    # 2 发起请求
    # get方法会返回一个响应对象
    response = requests.get(url=url)
    # 3 获取响应数据,text方法返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # 4 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！！！')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

