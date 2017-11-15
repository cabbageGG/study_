#!/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

'''
BeautifukSoup 4 大对象
Tag--name，attrs 两大属性
NavigableString--标签的内容，使用.string 属性获得
BeautifulSoup---表示一个文档的全部内容，也可以当作tag
Comment--是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号

常用命令 find_all('str') 可以传入正则，方法等
'''

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,'html.parser')

#soup = BeautifulSoup(open('index.html'))

#print soup.prettify()

links = soup.find_all('a')

print type(links)

