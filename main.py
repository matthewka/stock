#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.append("./py-libs/")
sys.path.append("./py-libs/dao")
from StockCrawler import StockCrawler
from LogTool import Log
from Config import Config

def main():
    #stocks = ["2317", "2303", "3481", "3019", "2330", "1455", "3576"]
    stocks = ["2317"]
    dates = ["20170101", "20170201", "20170301", "20170401", "20170501", "20170601", "20170701", "20170801", "20170901", "20171001", ]
    # for stock in stocks:
    #     for date in dates:
    #         crawler = StockCrawler(stock, date)
    #         crawler.run()

    # crawler = StockCrawler("2317", "20170101")
    # crawler.run()

    print(Config().DEBUG)

if __name__ == '__main__':
	main()