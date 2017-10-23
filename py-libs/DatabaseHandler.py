#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from LogTool import Log

class DatabaseHandler:

    log = Log()

    def __init__(self, name):
        global conn
        if len(name) > 0:
            conn = sqlite3.connect(name)
        else:
            conn = sqlite3.connect('./database/stock.db')

        self.createStockTable()


    def ensureTable(self, tableName):
        hasTable = True
        try:
            sqlCmd = "SELECT * from " + tableName
            cur = conn.cursor()
            cur.execute(sqlCmd)
        except Exception as e:
            self.log.loge(e)
            hasTable = False

        if not hasTable:
            self.createS_Table(tableName)

    def queryTable(self, tableName, column):
        sqlCmd = "SELECT " + column + " FROM " + tableName + ";"
        c = conn.cursor()
        cursor = c.execute(sqlCmd)
        return cursor

    def insertTable(self, tableName, keyString, valString):
        self.ensureTable(tableName)
        global conn

        sqlCmd = "INSERT INTO " + tableName + " " + keyString + " VALUES (" + valString + ")"
        cur = conn.cursor()
        cur.execute(sqlCmd)
        conn.commit()

    def createS_Table(self, tableName):
        global conn

        sqlCmd = "CREATE TABLE IF NOT EXISTS " + tableName + " (s_num TEXT, date TEXT, shares INT, amount INT, \
        open REAL, high REAL, low REAL, close REAL, spreads REAL, turnover INT, newest INT);"
        conn.execute(sqlCmd)

    def createStockTable(self):
        global conn
        sqlCmd = "CREATE TABLE IF NOT EXISTS stock (s_num TEXT, s_name TEXT, price REAL);"
        conn.execute(sqlCmd)

    def hasStockTable(self):
        global conn
        try:
            sqlCmd = "SELECT *, COUNT(*) FROM stock;"
            c = conn.execute(sqlCmd)
            result = c.fetchone()
            number_of_rows = result[0]
            print(number_of_rows)
            if not number_of_rows == None and int(number_of_rows) > 0:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False