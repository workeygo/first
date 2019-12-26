# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2016-7-27
@author: Jennifer
Project:使用unittest框架编写测试用例思路
'''
# 3.导入unittest模块
import unittest
from Utils.HTMLTestRunner import HTMLTestRunner
import re,requests,json,time


# 4.定义测试类，父类为unittest.TestCase。
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法。
class Test(unittest.TestCase):
    # def post(self, headers,url,body):
    #     if headers is None:
    #         headers = {
    #             "Content-Type": "application/json",
    #             "afs": "free",
    #             "Connection":"keep-alive",
    #             "Host":"bmspctest2.myxyzq.com"
    #         }
    #     if url is None:
    #         url = "https://nethalltest2.myxyzq.com/api/netway/user/fast"
    #     s = requests.session()
    #     content = s.post(url=url, headers=headers, data=body).text
    #     return content


    # 5.定义setUp()方法用于测试用例执行前的初始化工作。
    # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    # 注意，输入的值为字符型的需要转为int型
    def setUp(self):
        print('Test Start')

    # 6.定义测试用例，以“test_”开头命名的方法
    # 注意，方法的入参为self
    # 可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    # 可定义多个测试用例
    # 最重要的就是该部分


    def test1_case(self):
        headers = {
            "Content-Type": "application/json",
            "afs": "free"
        }
        url = "https://nethalltest2.myxyzq.com/api/netway/user/fast"
        body = json.dumps({
            'region_code': '86',
            'type': 1,
            'captcha': 8888,
            'phone': 12345678962
        })
        global userId,s,session
        s = requests.session()
        result = json.loads(s.post(url=url,headers=headers,data=body).text)
        userId= result['body']['userId']
        session = result['body']['session']
        print(result)
        self.assertEqual(result['message'], 'success', msg='message不等于success' )

    # @unittest.skip('暂时跳过用例1的测试')
    def test2_case(self):
        headers = {
            "Content-Type":"application/x-www-form-urlencoded;charset=utf-8",
            "afs":"free",
            "Connection":"keep-alive"
        }
        url = "https://bmspctest2.myxyzq.com/api/bmsAPI/security/market"
        body = {
              'user_id':userId
        }
        result = json.loads(s.post(url=url,headers=headers,data=body).text)
        print(result)
        self.assertEqual(result['message'],'success',msg='message不等于success')
    def test3_case(self):
        headers = {
            "Content-Type": "application/json",
            "afs": "free",
            "Connection": "keep-alive",
            "session":session
        }
        url = "https://nethalltest2.myxyzq.com/api/netway/quot/info"
        body = {

        }
        result = json.loads(s.get(url=url,headers=headers).text)
        print(result)
        self.assertEqual(result['message'],'success',msg='message不等于success')

    # 7.定义tearDown()方法用于测试用例执行之后的善后工作。
    # 注意，方法的入参为self
    def tearDown(self):
        print('Test over')


# 8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__ == '__main__':
    # 8.1执行测试用例方案一如下：
    # unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
    # 执行顺序是命名顺序：先执行test_case1，再执行test_case2
    # unittest.main()
    suit = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(Test))
    with open('../Report/'+'report.htm','wb') as f:
        HTMLTestRunner(stream=f,title=u'标题',description=u'描述').run(suit)
