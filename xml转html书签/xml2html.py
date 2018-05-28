# -*- coding: utf-8 -*-
"""
2018-04-03
手机xml书签转html通用书签

XML文件格式介绍：
<tag attrib = > text </tag> tail
例：<APP_KEY channel = 'CSDN'> hello123456789 </APP_KEY>

tag，即标签，用于标识该元素表示哪种数据，即APP_KEY
attrib，即属性，用Dictionary形式保存，即{'channel' = 'CSDN'}
text，文本字符串，可以用来存储一些数据，即hello123456789
tail，尾字符串，并不是必须的。

ElementTree解析XML文件的过程：
导入ElementTree，import xml.etree.ElementTree as ET
解析Xml文件找到根节点：
直接解析XML文件并获得根节点，tree = ET.parse('country_data.xml') root = tree.getroot()
解析字符串，root = ET.fromstring(country_data_as_string)
遍历根节点可以获得子节点，然后就可以根据需求拿到需要的字段了。

"""
import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='7.xml')

# 存储网站标题和网址
title = []
url = []
for elem in tree.iter(tag='title'):
    temp = elem.text.strip()
    temp_go = temp.replace('#','')
    title.append(temp_go)
    
for elem_url in tree.iter(tag='url'):
    temp = elem_url.text.strip()
    temp_go = temp.replace('#','')
    url.append(temp_go)

# 书签添加时间 逐步增加
date = 1476940005
with open('output.html','wt',encoding='utf-8') as f:
    #写入html头部
    f.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">')
    f.write('\n<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1>')
    f.write('\n<DL><p>\n')
    #写入书签
    for i in range(len(title)):
        f.write('\t<DT><A HREF="'+url[i]+'"' + ' ADD_DATE="' + str(date+i)+'">' + title[i] + '</A>')
        f.write('\n')
    #写入尾部
    f.write('</DL><p>')
