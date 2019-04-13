# coding:utf-8
import requests
import json
import random
from urllib import parse
import hashlib
import datetime


class RunMethod:
    def post_main(self, url, request_data, header=None):
        # 1.urlDecode解码
        #request_data = request_data[7:]
        #request_data = parse.unquote(request_data, 'utf-8')
        #request_data = json.loads(request_data)
        print(request_data)

        # 2.sessionkey重新加密
        randoms = str(random.randint(100, 999))
        request_data['random'] = randoms
        m = hashlib.md5()
        url_short = url[24:]
        md5_str = url_short + "UP360_sysion" + randoms
        m.update(md5_str.encode("utf8"))
        request_data['sessionKey'] = m.hexdigest() + ";984e5e9b9563036ae224b193d18a67a5;10144791"

        # 3.具体业务自定义
        # 3.1 布置作业业务
        if 'startTime' in request_data['params'].keys():
            start_time = datetime.datetime.now()
            end_time = start_time+datetime.timedelta(days=1)
            request_data['params']['startTime'] = start_time.strftime("%Y-%m-%d %H:%M:%S")
            request_data['params']['endTime'] = end_time.strftime("%Y-%m-%d %H:%M:%S")
        # 3.2 作业名称
        if 'homeworkName' in request_data['params'].keys():
            request_data['params']['homeworkName'] = request_data['params']['homeworkName'] + "_" + randoms
        # 3.3 作业名称
        if 'homeworkContent' in request_data['params'].keys():
            request_data['params']['homeworkContent'] = request_data['params']['homeworkContent'] + "_" + randoms
        # 3.4 学校通知业务
        if 'content' in request_data['params'].keys():
            request_data['params']['content'] = request_data['params']['content'] + "_" + randoms

        # 4.urlencode编码
        request_data = json.dumps(request_data)
        request_data = parse.quote(request_data, 'utf-8')
        request_data = 'moJson=' + request_data
        request_data = request_data.replace('%2B', '+')
        print("--->:" + request_data)

        # 5.提交post请求
        result = None
        if header != None:
            result = requests.post(url=url, data=request_data, headers=header)
        else:
            result = requests.post(url=url, data=request_data)

        return result.json()

    def get_main(self, url, request_data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=request_data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=request_data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False)
# return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    url = "https://mobile.up360.com/um/0/3"
    data = {"appId":"3286435","manufacturer":"OPPO","model":"OPPO R9m","params":{"account":"13867429835","checkBdeviceLogin":"1","password":"e10adc3949ba59abbe56e057f20f883e"},"random":15357,"sessionKey":"9ab7303cfaa8332effd27cd46780f381;ffffffff-f9d0-34d8-cf12-c9b17e4f7e97;","sysType":"3","sysVersion":"5.1","version":"4.1.5"}
    r = RunMethod()
    res = r.run_main("Post", url, data, {'Content-Type':'application/x-www-form-urlencoded'})
    print(res)
