# coding:utf-8
import MySQLdb.cursors
import json
import datetime


class OperationMysql:
    def __init__(self, db='up360_olclass'):
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

    # 查询一条数据
    def search_all(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
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
    sql = """SELECT  t.article_id  AS articleId, t.category_id AS categoryId, t.hits, 
            t.publish_time AS publishTime,t.image,t.title,c.category_name AS categoryName,
            t.sticky,IF(IFNULL(ar.article_id,0)=0 , 0, 1) AS readStatus
            FROM   s_parent_article t LEFT JOIN s_parent_article_category c ON t.category_id = c.category_id
           LEFT JOIN u_parent_article_read ar ON (t.article_id = ar.article_id and ar.user_id = 7943384)
            WHERE t.status = '1' ORDER BY t.sticky desc, t.publish_time DESC  LIMIT 20"""
    res = op_mysql.search_all(sql)
    print(res)
