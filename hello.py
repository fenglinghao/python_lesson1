#!/usr/bin/python3
#codeing = utf-8

import string
import urllib.request as request
import urllib.parse as parse

from bs4 import BeautifulSoup

def url_save_img(url, page_index):
    jpgNum = 1

    response = request.urlopen(url + str(page_index))
    html = response.read()
    data = html.decode('utf-8')
    soup = BeautifulSoup(data, "html.parser")

    for list in soup.find_all('img'):
        dict = list.attrs
        if "src" in dict:
            image = dict['src']
            if image.startswith("http") != True:
                continue
            index  = image.rfind('.')
            index1 = image.rfind('jpg')
            jpgurl = image[:index1 + 3]

            if index1 > 0 and (index1 == index + 1):
                filePath = './res/' + str(jpgNum) + '.jpg'
                with open(filePath, 'wb') as file:
                    try:
                        image_data = request.urlretrieve(jpgurl, filePath)
                    except:
                        file.close()
                        continue
                jpgNum += 1
                file.close()


if __name__ == "__main__":
    url = "https://tieba.baidu.com/p/1771502504?pn="

    page_start = 1
    page_end   = 32

    for i in range(page_start, page_end):
        url_save_img(url, i)


