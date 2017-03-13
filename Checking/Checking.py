#!/bin/env python
# coding=utf-8
import urllib2
import Image
import cStringIO
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def ImageScale(url):
  file = cStringIO.StringIO(urllib2.urlopen(url).read())
  img = Image.open(file)
  img.show()

if __name__ == "__main__":
   #python3.3
    file = open('LIST.TXT')

    lines = file.readlines()
    filename = []
    list = []
    for line in lines:
        temp = line[0:-1]
        filename.append(temp)
    print filename
    file2 = open('Lyu.txt','w')
    for i in filename:
        file = open(i)
        s = json.load(file)
        print 'https://item.taobao.com/item.htm?id='+s["id"]+'&ns=1&abbucket=12#detail'
        title = json.dumps(s["title"], ensure_ascii=False)
        print title
        img = json.dumps(s["img"], ensure_ascii=False)
        print img
        #print list
        try:

            bizResult = json.dumps(s["attributes"], ensure_ascii=False)
            attr = json.loads(bizResult)
            bizResult = json.dumps(attr.keys(), ensure_ascii=False)
            print s["id"]
            bizResult = bizResult.replace('"','').replace('[','').replace(']','')
            print bizResult

            list.append(i[0:-5])
            list.append(';')
            list.append(raw_input("请输入人工分类:".decode('utf-8')))
            list.append(';')
            list.append(bizResult)


            a = ''
            for i in range(len(list)):
                a+=str(list[i])
            a+='\n'
            #a+=str(list[len(list)-1])
            file2.writelines(a)
            file2.flush()
            print a
            #
            #print bizResult[0]
            #print
            list = []

        except:
            list.append(i[0:-5])
            list.append(';')
            list.append(raw_input("请输入人工分类:".decode('utf-8')))
            list.append(';')
            a = ''
            for i in range(len(list)):
                a+=str(list[i])
            a+='\n'
            file2.writelines(a)
            file2.flush()
            print a
            list = []




