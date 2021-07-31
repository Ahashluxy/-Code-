import requests
import json

if __name__ == '__main__':
    # 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 请求之前进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    #
    word = input('enter a word:')
    data = {
        'kw': word
    }
    # 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据:json()方法返回的是对象obj，但是得事先确认响应数据是json类型的才能用这个方法
    dic_obj = response.json()
    print(dic_obj)

    # 进行持久化存储
    fileName = word+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    # ensure_ascii=False返回的json数据有中文要指定ascii为false
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('word done!')
