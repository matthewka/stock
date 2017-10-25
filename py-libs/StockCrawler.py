#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import requests

import sys
sys.path.append("./dao")
import json
from DatabaseHandler import DatabaseHandler
from LogTool import Log
from dao_stock import stock

QUERY_URL = "http://www.tse.com.tw/exchangeReport/STOCK_DAY"

INDEX_DATE      = 0 #u日期
INDEX_SHARES    = 1 #u成交股數
INDEX_AMOUNT    = 2 #u成交金額
INDEX_OPEN      = 3 #u開盤價
INDEX_HIGH      = 4 #u最高價
INDEX_LOW       = 5 #u最低價
INDEX_CLOSE     = 6 #u收盤價
INDEX_SPREADS   = 7 #u漲跌價差
INDEX_TURNOVER  = 8 #u成交筆數


class StockCrawler(object):
    log = Log()

    def __init__(self):
        global dbHandler
        dbHandler = DatabaseHandler('')


    def run(self, stock_num, date):
        self.stockNum = stock_num
        self.date = date
        timestamp = int(time.time() * 1000 + 1000000)
        query_url = '{}?response=json&date={}&stockNo={}&_={}'.format(QUERY_URL, self.date, self.stockNum, timestamp)
        self.log.logv(query_url)
        try:
            req = requests.session()
            req.get('http://mis.twse.com.tw/stock/index.jsp',
                    headers={'Accept-Language': 'zh-TW',
                             'Content-Type':'application/json;charset=UTF-8}',
                             'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) \
                             AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36'})

            response = req.get(query_url)
            #print(response.text)
            content = json.loads(response.text)
            if 'data' in content.keys():
                datas = content['data']
            else:
                self.log.loge(content)
                datas = content['data']

            tableName = "s_" + self.stockNum

            for data in datas:
                s = stock(self.stockNum, data)
                global dbHandler
                dbHandler.insertOrUpdateTable(tableName, s.getKeyArray(), s.getValArray(), "date", s.getDate())
        except Exception as e:
            self.log.loge(query_url)
            self.log.loge(e)

    def run_stock_list(self):
        timestamp = int(time.time() * 1000 + 1000000)
        count = 0
        for i in range(1, 31):
            query_url = "{}?filter={:0>2}&_={}".format("http://www.tse.com.tw/zh/api/codeFilters", i, timestamp)

            try:
                req = requests.session()
                req.get('http://mis.twse.com.tw/stock/index.jsp',
                        headers={'Accept-Language': 'zh-TW',
                                 'Content-Type': 'application/json;charset=UTF-8}',
                                 'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) \
                                 AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36'})

                response = req.get(query_url)
                content = json.loads(response.text)
                datas = content['resualt']

                for data in datas:
                    sp = data.split('\t')
                    s_num = sp[0]
                    s_name = sp[1]
                    Log().logv("s_num = %s, s_name = %s" % (s_num, s_name))
                    count += 1
                    tableName = "stock"
                    keyArray = ["s_num", "s_name"]
                    valArray = ["'" + s_num + "'", "'" + s_name + "'"]
                    global dbHandler
                    dbHandler.insertOrUpdateTable(tableName, keyArray, valArray, "s_num", s_num)
            except Exception as e:
                self.log.loge(e)