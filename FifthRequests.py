import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    kw = input('enter a city to query:')
    param = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    response = requests.post(url=url, data=param, headers=headers)
    dic_js = response.text
    print(dic_js)
    fp = open('./kfc.json', 'w', encoding='utf-8')
    json.dump(dic_js, fp=fp, ensure_ascii=False)
    print('work done!')
