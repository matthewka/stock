#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from LogTool import Log

class DatabaseHandler:

    def __init__(self, name):
        global conn
        if len(name) > 0:
            conn = sqlite3.connect(name)
        else:
            conn = sqlite3.connect('./database/stock.db')

    def ensureTable(self, stockNum):
        hasTable = True
        try:
            sqlCmd = "SELECT * from s_" + stockNum
            cur = conn.cursor()
            cur.execute(sqlCmd)
        except Exception as e:
            Log().loge(e)
            hasTable = False

        if not hasTable:
            self.createTable(stockNum)


    def insertTable(self, stockNum, keyString, valString):
        self.ensureTable(stockNum)
        global conn

        sqlCmd = "INSERT INTO s_" + stockNum + " " + keyString + " VALUES (" + valString + ")"
        cur = conn.cursor()
        cur.execute(sqlCmd)
        conn.commit()

    def createTable(self, stockNum):

        global conn

        tableName = "s_" + stockNum
        sqlCmd = "CREATE TABLE IF NOT EXISTS " + tableName + " (s_num TEXT, date TEXT, shares TEXT, amount TEXT, \
        open REAL, high REAL, low REAL, close REAL, spreads TEXT, turnover TEXT);"
        conn.execute(sqlCmd)