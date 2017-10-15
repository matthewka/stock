#!/usr/bin/python
# -*- coding: utf-8 -*-

from LogTool import Log

class stock(object):

    INDEX_DATE = 0  # u日期
    INDEX_SHARES = 1  # u成交股數
    INDEX_AMOUNT = 2  # u成交金額
    INDEX_OPEN = 3  # u開盤價
    INDEX_HIGH = 4  # u最高價
    INDEX_LOW = 5  # u最低價
    INDEX_CLOSE = 6  # u收盤價
    INDEX_SPREADS = 7  # u漲跌價差
    INDEX_TURNOVER = 8  # u成交筆數

    date = ""
    shares = ""
    amount = ""
    open = ""
    high = ""
    low = ""
    close = ""
    spreads = ""
    turnover = ""

    dataArray = []

    def __init__(self, stock_num, data):
        global dataArray
        dataArray = data
        self.stockNum = stock_num
        self.parsing()

    def parsing(self):
        global date
        global shares
        global amount
        global open
        global high
        global low
        global close
        global spreads
        global turnover
        global dataArray

        try:
            date = dataArray[self.INDEX_DATE]
            shares = dataArray[self.INDEX_SHARES]
            amount = dataArray[self.INDEX_AMOUNT]
            open = dataArray[self.INDEX_OPEN]
            high = dataArray[self.INDEX_HIGH]
            low =  dataArray[self.INDEX_LOW]
            close =  dataArray[self.INDEX_CLOSE]
            spreads = dataArray[self.INDEX_SPREADS]
            turnover = dataArray[self.INDEX_TURNOVER]

        except Exception as e:
            Log().loge(e)

    def getKeyString(self):
        return "(s_num, date, shares, amount, open, high, low, close, spreads, turnover)"

    def getValString(self):
        valString = ""
        try:
            for i in range(0, 10):
                if i == 0:
                    dataStr = "'" + self.stockNum + "'"
                else:
                    if "--" == dataArray[i-1]:
                        dataArray[i-1] = "0"

                    if i == 1 or i == 2 or i == 3 or i == 8 or i == 9:
                        dataStr = "'" + dataArray[i - 1] + "'"
                    else:
                        dataStr = dataArray[i - 1]

                valString += dataStr
                if (i < 9):
                    valString += ", "
        except Exception as e:
            Log().loge(valString)
            Log().loge(e)

        return valString

    def getInsert(self):
        global dataArray
        try:
            keyString = ""
            valString = ""
            for i in range(0, 10):
                if i == 0:
                    dataStr = "'" + self.stockNum + "'"
                else:
                    if "--" == dataArray[i-1]:
                        dataArray[i-1] = 0

                    if i == 1 or i == 2 or i == 3 or i == 8 or i == 9:
                        dataStr = "'" + dataArray[i - 1] + "'"
                    else:
                        dataStr = dataArray[i - 1]

                valString += dataStr
                if (i < 9):
                    valString += ", "

            global dbHandler
            dbHandler.insertTable(self.stockNum, keyString, valString)
        except Exception as e:
            Log().loge(e)
            Log().loge(valString)

    def __str__(self):

        print(u'日期: %s' % date)
        print(u'成交股數: %s' % shares)
        print(u'成交金額: %s' % amount)
        print(u'開盤價: %s' % open)
        print(u'最高價: %s' % high)
        print(u'最低價: %s' % low)
        print(u'收盤價: %s' % close)
        print(u'漲跌價差: %s' % spreads)
        print(u'成交筆數: %s' % turnover)
        return "test"