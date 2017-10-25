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

    def insertTable(self, tableName, keyArray, valArray):
        try:
            self.ensureTable(tableName)
            global conn

            keyString = "("
            valString = "("

            keyLen = len(keyArray)
            for index in range(0, keyLen):
                keyString += keyArray[index]
                if index + 1 < keyLen:
                    keyString += ","
                else:
                    keyString += ")"

            valLen = len(valArray)
            for index in range(0, valLen):
                valString += valArray[index]
                if index+1 < keyLen:
                    valString += ","
                else:
                    valString += ")"


            sqlCmd = "INSERT INTO " + tableName + " " + keyString + " VALUES " + valString + ";"
            #print(sqlCmd)
            cur = conn.cursor()
            cur.execute(sqlCmd)
            conn.commit()
        except Exception as e:
            print(sqlCmd)
            print(e)

    def updateTable(self, tableName, keyArray, valArray, key, value):
        try:
            self.ensureTable(tableName)
            global conn

            paramString = ""
            paramLen = len(keyArray)
            for index in range(0, paramLen):
                paramString += keyArray[index]
                paramString += "="
                paramString += valArray[index]

                if index+1 < paramLen:
                    paramString += ","

            sqlCmd = "UPDATE " + tableName + " SET " + paramString + \
                     " WHERE " + key + "=" + value
            #print(sqlCmd)
            cur = conn.cursor()
            cur.execute(sqlCmd)
            conn.commit()
        except Exception as e:
            print(sqlCmd)
            print(e)

    def insertOrUpdateTable(self, tableName, keyString, valString, key, value):
        sqlCmd = "SELECT COUNT(*) FROM " + tableName + " WHERE " + key + "='" + value + "'"
        #print("insertOrUpdateTable: %s" % sqlCmd)
        try:
            cursor = conn.execute(sqlCmd)
            result = cursor.fetchone()
            num = result[0]
        except Exception as e:
            num = 0

        #print("num %d" % num)
        if not num == None and int(num) > 0: # update table
            #print("updateTable")
            self.updateTable(tableName, keyString, valString, key, value)
        else: #insert table
            #print("insertTable")
            self.insertTable(tableName, keyString, valString)

    def createS_Table(self, tableName):
        global conn

        sqlCmd = "CREATE TABLE IF NOT EXISTS " + tableName + " (s_num TEXT, date TEXT, shares INT, amount INT, \
        open REAL, high REAL, low REAL, close REAL, spreads REAL, turnover REAL, newest INT);"
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