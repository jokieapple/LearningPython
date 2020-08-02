# -*- coding:utf-8 -*-
# author: Jay time:2020/8/2
'''
制作一个汉字转换拼音的窗体，包含了按钮，单行输入框
'''

from tkinter import Tk,Entry,Button
import pinyin

#创建一个convert的函数，用来转换汉子成为拼音
def convert():
    #首先定义一个变量s，值为从文本框ent_hanzi中读取的文字
    s = ent_hanzi.get()
    #然后定义变量p，值为s汉字所对应的拼音
    p = pinyin.get(s)
    #接着向ent_pinyin文本框的最后插入拼音文本p
    ent_pinyin.insert('end' , p)
    return

#创建一个Tk（窗体）对象，并把它赋值给变量fm_main，于是可用fm_main代表该窗体
fm_main = Tk()
#创建显示空间对象，例如单行文本框类型对象名Entry
#再创建一个按钮对象Button
ent_hanzi = Entry(fm_main)
ent_pinyin = Entry(fm_main)
btn = Button(fm_main,text='点击显示拼音',command=convert)
#pack的顺序决定了控件类对象在窗体中显示的顺序
ent_hanzi.pack()
btn.pack()
ent_pinyin.pack()
#创建完所有窗体后，应当再调用mainloop()方法，才能确保窗体正常使用
fm_main.mainloop()

