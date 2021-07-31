
import re
import os
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    # 创建一个文件夹以存储图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    # 爬取糗百热图所有图片
    # 设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pageNum in range(1, 11):
        # 对应页码的url
        new_url = format(url%pageNum)

        # 使用通用爬虫对一整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text
        # 使用聚焦爬虫对页面中的所有图片进行解析
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)
        # print(img_src_list)
        for src in img_src_list:
            # 拼接完整的图片地址
            src = 'https:'+src
            # 请求到了二进制图片的数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            imgPath = './qiutuLibs/'+img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功')


