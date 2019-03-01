# coding:utf-8
import os
import sys
import unittest
import HTMLTestRunner
import time
from case.test_case import ApiTestCase
sys.path.append("D:/Python/workspace/APIAutoTestForUp360/")


class RunTest:
    # 获取测试用例集
    def create_suite(self):
        # 定义单元测试容器
        suite = unittest.TestSuite()
        suite.addTest(ApiTestCase('go_on_run'))
        return suite

    # 运行测试用例
    def run_suite(self):
        suite = self.create_suite()
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        file_path = os.getcwd() + "\\report\\" + day

        file_name = now + "_result.html"
        if os.path.exists(file_path):
            file_path = file_path + "\\" + file_name
        else:
            os.makedirs(file_path)
            file_path = file_path + "\\" + file_name

        fp = open(file_path, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'向上网接口api自动化测试报告', description=u'执行情况:')
        runner.run(suite)
        fp.close()
        print("-----------执行结束-----------")


if __name__ == '__main__':
    run = RunTest()
    run.run_suite()

