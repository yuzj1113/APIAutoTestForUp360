# coding:utf-8
import requests
import json


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)

        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
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
    data = "moJson=%7B%22random%22%3A%2271898%22%2C%22sessionKey%22%3A%22f959ac3c85c8b75e7bae0a4de9fe1508%3Bf3095f234df8b32efb79236d278b1bcf%22%2C%22manufacturer%22%3A%22apple%22%2C%22params%22%3A%7B%22account%22%3A%2215394215055%22%2C%22checkBdeviceLogin%22%3A%221%22%2C%22password%22%3A%22e10adc3949ba59abbe56e057f20f883e%22%7D%2C%22model%22%3A%22iPhone7%2C2%22%2C%22appId%22%3A%223286435%22%2C%22version%22%3A%224.1.2%22%2C%22sysVersion%22%3A%2212.1.2%22%2C%22sysType%22%3A%224%22%7D"

    r = RunMethod()
    res = r.run_main("Post", url, data, {'Content-Type':'application/x-www-form-urlencoded'})
    print(res)
