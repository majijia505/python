#!/bin/env python
#!encoding:utf-8
from xml.dom import minidom ,Node
#创建doc对象
doc = minidom.Document()
#创建comment对象---说明
comment = minidom.Comment("this is a test xml comment")

doc.appendChild(comment)
print doc.toprettyxml(indent='')
p_list = []
greate_parent = doc.createElement('greate_parent')
for i in range(10):
    parent = doc.createElement('parent%d' %i)
    parent.setAttribute('id','%d' %i)
    for j in range(10):
        child = doc.createElement('child')
        str = '%d' %j
        text = doc.createTextNode(str)
        #text.data=str
        child.appendChild(text)
        parent.appendChild(child)
    #print "this is a test parent"
    #print parent.toprettyxml(indent='')
    p_list.append(parent)
#    doc.appendChild(parent)    
print "the length of p_list is :%d" %len(p_list)
for i in p_list:
    greate_parent.appendChild(i)
    
doc.appendChild(greate_parent)    
    
print doc.toprettyxml()

