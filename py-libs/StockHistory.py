#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import datetime
import numpy as np

sys.path.append("./py-libs/")
from StockCrawler import StockCrawler
from GoogleFinCrawler import GoogleFinCrawler
from DatabaseHandler import DatabaseHandler
from LogTool import Log
import Config

class StockHistory():
    log = Log()

    def __init__(self, stockNum):
        global sc
        sc = StockCrawler()
        global gc
        gc = GoogleFinCrawler()
        global dbHelper
        dbHelper = DatabaseHandler('')

        self.stockNum = stockNum
        self.dbName = "s_" + stockNum
        self.today = datetime.datetime.now()
        self.syncHistory()

    def syncHistory(self):
        self.log.logv("syncHistory: %s" % self.stockNum)
        print("syncHistory: %s" % self.stockNum)
        global sc
        global gc
        global dbHelper
        preCount = 0
        dbCount = int(dbHelper.getCount(self.dbName))
        print("preCount: %d, dbCount: %d" % (preCount, dbCount))
        try:
            # while preCount == 0 or dbCount < Config.DB_RECORD_SIZE:
            #     fetchDate = self.getFetchDate(preCount)
            #     gc.fetch(self.stockNum, fetchDate)
            #     preCount += 1
            #     dbCount = dbHelper.getCount(self.dbName)
            #
            # #self.delOldRecord(dbCount - Config.DB_RECORD_SIZE)

            fetchDate = self.getFetchDate(preCount)
            gc.fetch(self.stockNum, fetchDate)

        except Exception as e:
            print(e)

    def delOldRecord(self, count):
        global dbHelper
        dates = dbHelper.query(self.dbName, "date", "ASC")

        for i in range(0, count):
            dbHelper.delete(self.dbName, ["date"], [dates[i]])

    def getFetchDate(self, preCount):
        year = self.today.year
        month = self.today.month

        for i in range(0, preCount):
            if month == 1:
                year -= 1
                month = 12
            else:
                month -= 1

        return '{}{:0>2}{:0>2}'.format(year, month, "01")

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
