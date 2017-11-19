# **coding: utf8**
"""
pip install pymysql
"""
import pymysql as MySQLdb


class DatabaseWrapper:

    def __init__(self, sitting_params):
        self.sitting_params = sitting_params

    def get_connection_params(self):
        return self.sitting_params

    def get_new_connect(self):
        # 获取连接参数
        params = self.get_connection_params()
        try:
            print("连接成功")
            return MySQLdb.connect(**params)
        except MySQLdb.Error:
            print("连接失败")

    def create_cursor(self):
        cursor = self.get_new_connect().cursor()
        print("创建游标")
        return CursorWrapper(cursor)


class CursorWrapper:

    def __init__(self, cursor):
        self.cursor = cursor

    def excute(self, query):
        try:
            return self.cursor.excute(query)
        except MySQLdb.OperatorError:
            print("操作错误")


settings_dict = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'VegetableFactory',
    'user': 'root',
    'password': 'mcc616254086',
    'charset': 'utf8'
}


conn = DatabaseWrapper(settings_dict).create_cursor()



