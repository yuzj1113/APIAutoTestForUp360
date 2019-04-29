# coding:utf-8
import sys
import json

sys.path.append('D:/Python/workspace/APIAutoTestForUp360/')
import random
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse


class DependdentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel(1, 'config/test_case.xls')
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)

        # header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, {'Content-Type': 'application/x-www-form-urlencoded'})
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        print(response_data)
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    order = {
        "data": {
            "userId": 9908685,
            "userType": "G"
        },
        "msg": "登录成功！",
        "result": "1",
        "testMsg": ""
        }

    res = "data.userId"
    json_exe = parse(res)
    id = [match.value for match in json_exe.find(order)][0]
    print(id)
