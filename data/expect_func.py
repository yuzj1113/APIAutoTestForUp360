# coding:utf-8
import json
from util.common_util import CommonUtil


class ExpectFunc:
    def __init__(self):
        self.commonUtil = CommonUtil()

    # 获取文章的方法
    def get_articles(self, data):
        data = json.loads(data)
        articles = []
        for article in data:
            article = {
			    "articleId": article["articleId"],
			    "categoryId": article["categoryId"],
			    "categoryName": article["categoryName"],
			    "detailUrl": "https://www.up360.com/home/parentArticle/detail?userId=10144791&appId=3286435&imei=984e5e9b9563036ae224b193d18a67a5&articleId="+ str(article["articleId"]),
			    "hits": article["hits"],
			    "image": "https://data.up360.com/" +article["image"],
			    "publishTime": article["publishTime"],
			    "readStatus": article["readStatus"],
			    "sticky": article["sticky"],
			    "title": article["title"],
		    }
            articles.append(article)

        data = {"data": {"articles": articles}, "msg": "", "result": "1", "testMsg": ""}
        expect_data = json.dumps(data)
        return expect_data
