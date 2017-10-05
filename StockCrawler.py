import time
import requests
import datetime
import json
import sqlite3

QUERY_URL = "http://www.tse.com.tw/exchangeReport/STOCK_DAY?"

INDEX_DATE      = 0 #日期
INDEX_SHARES    = 1 #成交股數
INDEX_AMOUNT    = 2 #成交金額
INDEX_OPEN      = 3 #開盤價
INDEX_HIGH      = 4 #最高價
INDEX_LOW       = 5 #最低價
INDEX_CLOSE     = 6 #收盤價
INDEX_SPREADS   = 7 #漲跌價差
INDEX_TURNOVER  = 8 #成交筆數


class StockCrawler(object):
    def __init__(self, stock_num, date):
        self.stockNum = stock_num
        self.date = date
        self.conn = sqlite3.connect('stock.db')


    def run(self):
        timestamp = int(time.time() * 1000 + 1000000)
        query_url = '{}?response=json&date={}&stockNo={}&_={}'.format(QUERY_URL, self.date, self.stockNum, timestamp)
        print("query_url")
        try:
            req = requests.session()
            req.get('http://mis.twse.com.tw/stock/index.jsp',
                    headers={'Accept-Language': 'zh-TW',
                             'Content-Type':'application/json;charset=UTF-8}',
                             'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) \
                             AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36'})

            response = req.get(query_url)
            # print(response.text)
            content = json.loads(response.text)
            datas = content['data']
            print(datas)

            self.createTable(self.stockNum)
            for data in datas:
                print(u'日期: %s' %data[INDEX_DATE])
                print(u'成交股數: %s' % data[INDEX_SHARES])
                print(u'成交金額: %s' % data[INDEX_AMOUNT])
                print(u'開盤價: %s' % data[INDEX_OPEN])
                print(u'最高價: %s' % data[INDEX_HIGH])
                print(u'最低價: %s' % data[INDEX_LOW])
                print(u'收盤價: %s' % data[INDEX_CLOSE])
                print(u'漲跌價差: %s' % data[INDEX_SPREADS])
                print(u'成交筆數: %s' % data[INDEX_TURNOVER])
                keyString = "(s_num, date, shares, amount, open, high, low, close, spreads, turnover)"
                valString = ""
                for i in range(0, 10):
                    if i == 0:
                        dataStr = "'" + self.stockNum + "'"
                    else:
                        if i == 1 or i == 2 or i == 3:
                            dataStr = "'" + data[i-1] + "'"
                        else:
                            dataStr = data[i-1]

                    valString += dataStr
                    if (i < 8):
                        valString += ", "

                self.insertTable(self.stockNum, keyString, valString)



        except Exception as e:
            print(e)

    def insertTable(self, stockNum, keyString, valString):
        sqlCmd = "INSERT INTO s_" + self.stockNum + " " + keyString + " VALUES (" + valString + ")"
        print(sqlCmd)
        cur = self.conn.cursor()
        cur.execute(sqlCmd)
        self.conn.commit()

    def createTable(self, stockNum):
        tableName = "s_" + stockNum
        sqlCmd = "CREATE TABLE IF NOT EXISTS " + tableName + " (s_num TEXT, date TEXT, shares TEXT, amount TEXT, \
        open REAL, high REAL, low REAL, close REAL, spreads REAL, turnover INTEGER);"
        self.conn.execute(sqlCmd)