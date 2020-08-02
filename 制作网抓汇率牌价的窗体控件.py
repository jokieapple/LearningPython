# -*- coding:utf-8 -*-
# author: Jay time:2020/8/2
'''
制作一个窗体控件，能显示从网站抓取的汇率信息，同时还能够保存文件到指定目录
'''

from tkinter import Tk,Entry,Button,Text
from urllib.request import  urlopen
from bs4 import  BeautifulSoup

#首先定义一个getdata的函数，使其能够从网站上抓取今日的中间结算价
def getdata():
    c = urlopen('https://www.boc.cn/sourcedb/whpj/').read()
    bs_obj = BeautifulSoup(c, features='lxml')
    all_tr = bs_obj.find_all('table')[1].find_all('tr')
    for s in all_tr[1:]:
        all_td = s.find_all('td')
        #这里for循环执行的结果是直接向text框体中插入想要的结果，而不是打印或者返回值
        t1.insert('end',f'{all_td[6].text}发布的{all_td[0].text}中间折算价为{all_td[5].text}\n')

#再定义一个savedata的函数，使其能将运行第一个函数返显后的结果保存在一个文件下
def savedata():
    f = open('D:\Jupyter_working_path\data\currency.txt','w')
    #这里，向新文件中写入的内容为t1这个文本框中得到的文字;1.0代表第一行第一列这个文字开始，'end'代表到最后。
    f.write(t1.get(1.0,'end'))
    f.close()

fm_main = Tk()
t1 = Text(fm_main)
b1 = Button(fm_main, text='获取当日中间价',command=getdata)
b2 = Button(fm_main, text='点击保存文件',command=savedata)
b1.pack()
b2.pack()
t1.pack()
# 创建完所有窗体后，应当再调用mainloop()方法，才能确保窗体正常使用
fm_main.mainloop()