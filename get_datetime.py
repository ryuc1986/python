# coding:utf-8

import datetime

print("DateTime")

today = datetime.datetime.today()
print(today)

datetimeformat = '{0:%Y}年{0:%m}月{0:%d}日{0:%H}時{0:%M}分{0:%S}秒'.format(today)
print(datetimeformat)

#######################################
date = datetime.datetime.today().date()
print(date)

dateyear = datetime.datetime.today().date().year
print(dateyear)

datemonth = datetime.datetime.today().date().month
print(datemonth)

dateday= datetime.datetime.today().date().day
print(dateday)

time = datetime.datetime.today().time()
print(time)


