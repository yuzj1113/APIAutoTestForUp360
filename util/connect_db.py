# coding:utf-8
import MySQLdb.cursors
import json
import datetime


class OperationMysql:
    def __init__(self, db='up360_user'):
        self.db = db
        self.conn = MySQLdb.connect(
            host='192.168.0.122',
            port=3306,
            user='root',
            passwd='123456',
            db=self.db,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result, cls=DateEncoder)
        return result


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("SELECT c.user_id FROM c_user c LEFT JOIN s_passwd s ON s.ciphertext = c. PASSWORD  WHERE c.mobile = '13867429835' AND c.user_type = 'G' AND s.plaintext = '123456'")
    print(res)
