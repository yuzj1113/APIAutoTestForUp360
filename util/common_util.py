# coding:utf-8
import json
import operator


class CommonUtil:
    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否再另外一个字符串中
        str_one:查找的字符串
        str_two：被查找的字符串
        '''

        flag = None

        if isinstance(str_one, str):
            str_one = str_one.encode('unicode-escape').decode('string_escape')
            return operator(str_one, str_two)

        if str_one in str_two:
            flag = True
        else:
            flag = False

        return flag

    def is_equal_dict(self, dict_one, dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
            print(dict_two)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
            print(dict_two)
        return operator.eq(dict_one, dict_two)

    def is_json(self, data):
        '''
        判断是否json格式
        '''
        try:
            json.loads(data)
        except ValueError:
            return False

        return True


if __name__ == '__main__':
    opers = CommonUtil()
    xx = {"data": {"userId": 7202309, "userType": "G"}, "msg": "登录成功！", "result": "1", "testMsg": ""}
    yy = {"data": {"userId": 7202309, "userType": "G"}, "msg": "登录成功！", "result": "1", "testMsg": ""}
    res = opers.is_equal_dict(xx, yy)
    print(res)
