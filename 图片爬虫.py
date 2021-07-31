import requests


if __name__ == '__main__':
    # 待爬取的图片地址
    url = 'https://pic.qiushibaike.com/system/pictures/12457/124573715/medium/IZIWSQ1S270WSDVP.jpg'
    # content方法返回的是二进制图片数据
    # text返回字符串 content二进制 json返回对象
    img_data = requests.get(url=url).content

    with open('./qiutu.jpg', 'wb') as fp:
        fp.write(img_data)
