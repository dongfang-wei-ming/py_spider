# _*_ coding: utf-8 _*_
# @Time: 2021/12/1 16:13 
# @Author: 叶刚诚
# @File: final
# @Project: py_spider
from selenium.webdriver.common.by import By

from handless import share_browser
import urllib.request
if __name__ == '__main__':

    brower=share_browser()

    url=input('请输入要爬的网站:')

    path=input('请输入图片存储文件夹(默认D:\spider):')

    if len(path)==0:
        path="D:\spider\\"
    else:
        path+="\\"

    brower.get(url)

    img_list=brower.find_elements('xpath','//img')

    i=1

    for img in img_list:
        url=img.get_attribute('src')
        urllib.request.urlretrieve(url,path+str(i)+'.jpg')
        print('在下载第'+str(i)+'个图片')
        i+=1
    brower.quit()
