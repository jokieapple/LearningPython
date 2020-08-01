# -*- coding:utf-8 -*-
# author: Jay time:2020/8/1
from urllib.request import  urlopen
from bs4 import  BeautifulSoup

r = urlopen('https://www.boc.cn/sourcedb/whpj/')
c = r.read()
bs_obj = BeautifulSoup(c,features='lxml')
#下面需要找到定位后的第二个table
t = bs_obj.find_all('table')[1]
#下面需要继续定位第二个table下的所有tr行
all_tr = t.find_all('tr')
#根据读取的结果，可以发现第一行tr不是我们想要的结果，所以删除掉
all_tr.pop(0)
for s in all_tr :
    all_td = s.find_all('td')
    #这里需要知道每个货币当天的买入价。货币名称是在第一列，中间折算价则是第6列
    print(f'{all_td[6].text}发布的{all_td[0].text}中间折算价为{all_td[5].text}')
