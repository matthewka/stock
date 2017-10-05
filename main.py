from StockCrawler import StockCrawler
import sqlite3



def main():
    stocks = ["2317", "2303", "3481", "3019", "2330", "1455", "3576"]
    dates = ["20170101", "20170201", "20170301", "20170401", "20170501", "20170601", "20170701", "20170801", "20170901", "20171001", ]
    # for stock in stocks:
    #     for date in dates:
    #         crawler = StockCrawler(stock, date)
    #         crawler.run()

    crawler = StockCrawler("2317", "20171001")
    crawler.run()


if __name__ == '__main__':
	main()