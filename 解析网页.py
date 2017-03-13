# _*_ coding:utf-8 _*_ 
import urllib2 
#import urllib
import re 
from bs4 import BeautifulSoup
import os, sys, urllib2,time,random,uuid
from PIL import Image




def crawl(url): 
        str1 = time.strftime('%Y-%m-%d %X',time.localtime()) 
        print (u'【抓取时间】') 
        print str1
        page = urllib2.urlopen(url) 
        contents = page.read() 
        soup = BeautifulSoup(contents,"html.parser") 
        print(u'【当前价格】') 
        Current_Prices = soup.find('em',class_='tb-rmb-num')
        for Price in Current_Prices:
            print Price.string
        
        print(u'【图片地址】') 
       
       # 创建文件夹
        path = os.getcwd()                        # 获取此脚本所在目录
        new_path = os.path.join(path,u'淘宝\\')
        if not os.path.isdir(new_path):
            os.mkdir(new_path)
            
        filename = 1
        Commodity_Pictures = soup.find_all('div',class_='tb-pic tb-s50')
        for Commodity_Pictures in Commodity_Pictures:
            jokes = Commodity_Pictures.find('img')
            link = jokes.get('data-src')
            flink = link
            print flink #图片原地址
            #content2 = urllib2.urlopen(flink[:-10]).read()
            print flink[:-10] #经过处理的图片的地址(去掉 _50x50.jpg 的部分以获得原图)
            
           
            #print new_path,str(filename),'.jpg'
            file=open(new_path+str(filename)+'.jpg','wb')
            filename = filename + 1
            file.write(flink)
            file.flush()
            file.close()
            
            

        print(u'【宝贝详情】') 
       
        for tag in soup.find_all('ul', class_='attributes-list'): 
           count = 0
           for tag2 in tag.find_all('li'):
                count= count + 1
                print count,tag2.string
                
                
if __name__ == '__main__': 
    crawl('https://item.taobao.com/item.htm?spm=a230r.1.14.96.7Vq15k&id=41897619021&ns=1&abbucket=18#detail')
    #crawl('https://item.taobao.com/item.htm?spm=a230r.1.14.59.NAkNRX&id=43689522960&ns=1&abbucket=18#detail')