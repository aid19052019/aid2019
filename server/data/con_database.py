import pymysql

class DataBase:
    def __init__(self):
        self.__HOST = "127.0.0.1"
        self.__PORT = 3306
        self.__USER = "mysql"
        self.__PASS = "123456"
        self.__DATABASE = "store"
        self.__CHARSET = "utf8"
        self.db = pymysql.connect(host = self.__HOST,
                                  port = self.__PORT,
                                  user = self.__USER,
                                  password = self.__PASS,
                                  database = self.__DATABASE,
                                  charset = self.__CHARSET)

    def create_cur(self):
        self.cur = self.db.cursor()
