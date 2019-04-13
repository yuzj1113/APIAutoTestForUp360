# coding:utf-8
import json
import random
from urllib import parse
from urllib import request

class OperetionJson:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = 'config/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]

    # 写json
    def write_data(self, data):
        with open('../config/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))

    def deal_data(self, request_data, key, value):
        #data = data[7:]
        #request_data = parse.unquote(data)
        #request_data = json.loads(request_data)
        if '.' in key:
            list = key.split('.')
            request_data[list[0]][list[1]] = value
        else:
            request_data[key] = value
        request_data['random'] = random.randint(10000, 99999)
        #request_data = json.dumps(request_data)
        #print(request_data)
        #request_data = parse.quote(request_data)
        #request_data = 'moJson=' + request_data
        return request_data


if __name__ == '__main__':
    opjson = OperetionJson('../config/user.json')
    data = "moJson=%7B%22appId%22%3A%223286435%22%2C%22manufacturer%22%3A%22vivo%22%2C%22model%22%3A%22vivo+Y83A%22%2C%22params%22%3A%7B%22userId%22%3A%22123456%22%7D%2C%22random%22%3A15969%2C%22sessionKey%22%3A%224ab63e6d489584586890c2937b6d8219%3B00000000-4ed1-486d-ffff-ffff9b73f65c%3B9908685%22%2C%22sysType%22%3A%223%22%2C%22sysVersion%22%3A%228.1.0%22%2C%22version%22%3A%224.1.2%22%7D"
    print(data)
    request_data = opjson.deal_data(data, 'params.userId', '654321')
    print(request_data)
