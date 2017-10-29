#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import datetime
import numpy as np

sys.path.append("./py-libs/")
from StockCrawler import StockCrawler
from DatabaseHandler import DatabaseHandler
import Config

class StockHistory():

    def __init__(self, stockNum):
        global sc
        sc = StockCrawler()
        global dbHelper
        dbHelper = DatabaseHandler('')

        self.stockNum = stockNum
        self.dbName = "s_" + stockNum
        self.today = datetime.datetime.now()
        self.syncHistory()

    def syncHistory(self):
        global sc
        global dbHelper
        preCount = 0
        try:
            while dbHelper.getCount(self.dbName) < Config.DB_RECORD_SIZE:
                fetchDate = self.getFetchDate(preCount)
                sc.fetch(self.stockNum, fetchDate)
                preCount += 1
        except Exception as e:
            print(e)

    def getFetchDate(self, preCount):
        year = self.today.year
        month = self.today.month

        for i in range(0, preCount):
            if month == 1:
                year -= 1
                month = 12
            else:
                month -=1

        return '{}{:0>2}{}'.format(year, month, "01")

    def getCloseHistory(self):
        return self.getHistory(column="close")

    def getOpenHistory(self):
        return self.getHistory(column="open")

    def getHighHistory(self):
        return self.getHistory(column="high")

    def getLowHistory(self):
        return self.getHistory(column="low")
        
        
    def getHistory(self, column):
        global dbHelper
        vals = dbHelper.getRecords(self.dbName, column=column)
        res = np.squeeze(np.array(vals, dtype=np.float64))

        return res
