import requests
# UA检测:网站的服务器会检测对应请求的载体身份标识、如果检测到请求的载体身份标识为某一款浏览器
# 说明该请求是一个正常请求。
# User-Agent
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36
# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
if __name__ == '__main__':
    # 伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    # 处理url携带的参数：封装到字典中
    url = 'https://www.sogou.com/web'
    kw = input('enter a Keyword:')
    param = {
        'query': kw
    }
    # 对指定的url发起请求的过程中url是携带参数的params可以指定参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    filename = kw+'.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename, '保存成功！！！')
