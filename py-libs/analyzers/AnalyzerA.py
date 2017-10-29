import talib as ta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from DatabaseHandler import DatabaseHandler
from StockHistory import StockHistory
import sqlite3

class AnalyzerA(object):
    def __init__(self):
        global dbHandler
        global conn
        dbHandler = DatabaseHandler('')
        conn = sqlite3.connect('./database/stock.db')
        np.set_printoptions(threshold=0)

    def analyze(self):
        sh = StockHistory("2317")
        closePrices = sh.getCloseHistory()
        highPrices = sh.getHighHistory()
        lowPrices = sh.getLowHistory()
        
        rsi5 = ta.RSI(closePrices, 5)
        rsi55 = ta.RSI(closePrices, 55)
        will5 = ta.WILLR(highPrices, lowPrices, closePrices, timeperiod=5)
        will55 = ta.WILLR(highPrices, lowPrices, closePrices, timeperiod=55)
        sma5 = ta.SMA(closePrices, timeperiod=5)
        sma13 = ta.SMA(closePrices, timeperiod=13)
        sma20 = ta.SMA(closePrices, timeperiod=20)
        sma21 = ta.SMA(closePrices, timeperiod=21)
        sma55 = ta.SMA(closePrices, timeperiod=55)
        sma60 = ta.SMA(closePrices, timeperiod=60)
        sma89 = ta.SMA(closePrices, timeperiod=89)
        sma144 = ta.SMA(closePrices, timeperiod=144)
        sma233 = ta.SMA(closePrices, timeperiod=233)
        sma377 = ta.SMA(closePrices, timeperiod=377)
        macd, macdsignal, macdhist = ta.MACD(closePrices, fastperiod=12, slowperiod=26, signalperiod=9)
        upperband, middleband, lowerband = ta.BBANDS(closePrices, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

        print("收盤價: {}".format(closePrices[-1]))
        print(sma5[-1])
        print(sma20[-1])
        print(sma60[-1])
        print(rsi5[-1])
        print(rsi55[-1])
        print(will5[-1])
        print(will55[-1])
        print(macd[-1])
        print(macdsignal[-1])
        print(macdhist[-1])
        print(upperband[-1])
        print(middleband[-1])
        print(lowerband[-1])


    def getStocks(self, stockNum):
        global conn
        stockTable = "s_" + stockNum
        sqlCmd = "SELECT close from " + stockTable + " ORDER BY date ASC"
        #sqlCmd = "SELECT close from " + stockTable + " ORDER BY date DESC"
        cursor = conn.execute(sqlCmd)
        values = cursor.fetchall()
        vals = []
        for value in values:
            vals.append(value)
        res = np.squeeze(np.array(vals, dtype=np.float64))
        return res


