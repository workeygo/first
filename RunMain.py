# coding=utf-8
'''
Created on 2018-4-26
@author: Andy
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，邮件始终不能显示html：将电脑时间改为北京时间即可
'''
from Config import Config
import unittest
from Utils.Get_File import Get_File
from Utils.Send_Email import Send_Email
from Utils.BeautifulReport.BeautifulReport import BeautifulReport
from Utils.HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':
    print('=====AutoTest Start======')
    # 1.执行测试用例，生成最新的测试用例
    # Windows的cmd执行：python "C:\Users\user\PycharmProjects\Interface_Test_Project\RunMain.py"
    # 不用绝对路径会报：ImportError: Start directory is not importable: './test_case'
    # 通过defaultTestLoader类下面的discover()方法可自动根据目录start_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例返回测试套件
    suite = unittest.defaultTestLoader.discover(Config.test_dir, pattern='test_*.py')
    # filename = Config.test_report_dir + '\\' + Config.now + 'report.html'
    # with open(filename, 'wb') as f:
    #     # 需以Unicode格式编码f对象的中文。否则在windows下执行会报：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 553: ordinal not in range(128)
    #     runner = HTMLTestRunner(stream=f, title=u'测试报告', description=u'用例执行情况：')
    #     # HTMLTestRunner.run() run方法入参为测试套件TestSuite
    #     runner.run(suite)
    BeautifulReport(suite).report(filename=Config.now +'report.html',description='用例执行情况:',report_dir=Config.test_report_dir)
    # 2.取最新测试报告
    new_report = Get_File().new_file(Config.test_report_dir)


    # 3.发送邮件，发送最新测试报告html
    Send_Email().send_email(new_report)
    print('=====AutoTest Over======')

    #docker logs -f test2_netway_web
    #docker ps
