#!/usr/bin/python
# -*- coding: utf-8 -*-

from LogTool import Log
import datetime

class stock(object):

    INDEX_DATE = 0  # u日期
    INDEX_CLOSE = 1  # u收盤價
    INDEX_HIGH = 2  # u最高價
    INDEX_LOW = 3  # u最低價
    INDEX_OPEN = 4  # u開盤價
    INDEX_VOLUME = 5 # u成交量

    date = "" # String
    open = "" # Float
    high = "" # Float
    low = "" # Float
    close = "" # Float

    dataArray = []

    def __init__(self, stock_num, data):
        global dataArray
        dataArray = data
        self.stockNum = stock_num
        self.parsing()

    def parsing(self):
        global date
        global open
        global high
        global low
        global close
        global dataArray

        try:
            #date = self.trimDate()
            dt = dataArray[self.INDEX_DATE]
            self.date = "{}{:0>2}{:0>2}".format(dt.year, dt.month, dt.day)
            self.open = dataArray[self.INDEX_OPEN]
            self.high = dataArray[self.INDEX_HIGH]
            self.low = dataArray[self.INDEX_LOW]
            self.close = dataArray[self.INDEX_CLOSE]

        except Exception as e:
            Log().loge(e)

    def getKeyArray(self):
        keyArray = ["s_num", "date", "open", "high", "low", "close"]
        return keyArray

    def getValArray(self):
        valArray = []
        try:
            for i in range(0, 6):
                if i == 0:
                    valArray.append("'" + self.stockNum + "'")
                else:
                    if "--" == dataArray[i-1]:
                        dataArray[i-1] = "0"

                    # if i == 1 or i == 2 or i == 3 or i == 8 or i == 9:
                    if i == 1:
                        dataStr = "'" + self.date + "'"
                    else:
                        dataStr = self.trim(dataArray[i - 1])

                    valArray.append(dataStr)
        except Exception as e:
            Log().loge(valArray)
            Log().loge(e)

        return valArray

    def trim(self, data):
        res = data.replace(",", "")
        res = res.replace("X", "")
        return res

    def getDate(self):
        return self.date

    def __str__(self):

        print(u'日期: %s' % self.date)
        print(u'開盤價: %s' % self.open)
        print(u'最高價: %s' % self.high)
        print(u'最低價: %s' % self.low)
        print(u'收盤價: %s' % self.close)
        return "test"