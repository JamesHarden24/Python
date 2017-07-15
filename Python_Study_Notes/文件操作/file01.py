# -*- coding:utf-8 -*-
'''
Created on 2017年7月12日

@author: Administrator
'''

fp = open('F:\\GitHub\\Python\\ReadMe.txt', 'r')
cont = fp.read() #read()函数将打开的文件全部读完

print cont

fp.close()

fp = open(r'F:\GitHub\Python\readme.txt', 'r')

'''
read()函数
read(n) n为要读取的字节数

readline()函数
读取一行，读到行末尾

readlines()函数返回值由字符串组成的列表
通过遍历字符串列表可以进行打印

文件同样是可迭代的 iter

'''
cont = fp.read() #read()函数将打开的文件全部读完

str_list = cont.split('\n')

print str_list

fp.close()

str1 = fp.readline()
print str1.strip('\n') #去除字符串的末尾的\n并打印




