#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time

sys.path.append("./py-libs/")
sys.path.append("./py-libs/dao")
from StockCrawler import StockCrawler
from DatabaseHandler import DatabaseHandler
from StockHistory import StockHistory
from Analyzer import Analyzer
from LogTool import Log
import Config
import time

def main():
    print("Start: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    startTime = time.time()
    dbHandler = DatabaseHandler('')
    crawler = StockCrawler()
    today = time.strftime("%Y%m%d", time.localtime())

    if not dbHandler.hasStockTable():
        print("run_stock_list")
        crawler.run_stock_list()

    stocks = []
    dates = []

    if Config.DEVELOP:
        stocks = ["2317"]
        # dates = ["20160701", "20160801", "20160901","20161001", "20161101", "20161201","20170101",
        #          "20170201", "20170301", "20170401", "20170501", "20170601", "20170701", "20170801",
        #          "20170901", "20171001"]
        # dates = ["20171001"]
        # for stock in stocks:
        #     for date in dates:
        #         crawler.run(stock, date)
    else:
        cursor = dbHandler.queryTable("stock", "*")
        # dates = ["20160701", "20160801", "20160901", "20161001", "20161101", "20161201", "20170101",
        #          "20170201", "20170301", "20170401", "20170501", "20170601", "20170701", "20170801",
        #          "20170901", "20171001"]
        # only update today's stock
        dates = [today]
        for row in cursor:
            stocks.append(row[0])
            # print("s_num = %s, s_name = %s" % (row[0], row[1]))


    # for stock in stocks:
    #     for date in dates:
    #         crawler.run(stock, date)

    endTime = time.time()

    print("End: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    analyzer = Analyzer()
    analyzer.run()

if __name__ == '__main__':
	main()