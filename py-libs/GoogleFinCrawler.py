import time
import requests

import sys
sys.path.append("./dao")
import json
from DatabaseHandler import DatabaseHandler
from datetime import datetime, timedelta
from LogTool import Log
from dao_google_fin import stock

class GoogleFinCrawler:
    log = Log()

    QUERY_URL = " http://finance.google.com/finance/getprices"

    def __init__(self):
        global dbHandler
        dbHandler = DatabaseHandler('')

    def fetch(self, stockNum, date):
        query_url = '{}?q={}&x=TPE&i=86400&p=5Y'.format(self.QUERY_URL, stockNum)
        #print(query_url)

        response = requests.get(query_url)
        tableName = "s_" + stockNum
        if response.status_code == 200:
            datas = self.parsing(response.text)

            for data in datas:
                if len(data) > 0:
                    s = stock(stockNum, data)
                    global dbHandler
                    dbHandler.insertOrUpdateTable(tableName, s.getKeyArray(), s.getValArray(), "date", s.getDate())
                else:
                    print("Do not parsing date due to its empty")
        else:
            print("API response: %d" % response.status_code)


    def parsing(self, response):
        lines = response.split('\n')
        firstRow = False
        startParsing = False
        initTime = datetime.today()
        result =[]
        for line in lines:
            if len(line) > 0:
                if line.startswith('a'):
                    firstRow = True
                    startParsing = False
                else:
                    firstRow = False

                data = []

                if firstRow:
                    # 找出起始行日期
                    splits = line.split(',')
                    initTime = datetime.fromtimestamp(int(splits[0][1:]))
                    data.append(initTime) # DATE
                    data.append(splits[1])  # CLOSE
                    data.append(splits[2])  # HIGH
                    data.append(splits[3]) # LOW
                    data.append(splits[4])  # OPEN
                    data.append(splits[5]) # VOLUME
                    result.append(data)
                    startParsing = True
                else:
                    if startParsing:
                        splits = line.split(',')
                        delta = int(splits[0])
                        data.append(initTime + timedelta(days=delta)) # DATE
                        data.append(splits[1])  # CLOSE
                        data.append(splits[2])  # HIGH
                        data.append(splits[3])  # LOW
                        data.append(splits[5])  # VOLUME
                        result.append(data)

        return result