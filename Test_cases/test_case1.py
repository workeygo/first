# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-12-11
@author: Olivia
Project:使用unittest框架编写测试用例思路
'''
# 3.导入unittest模块
import unittest
from Utils.HTMLTestRunner import HTMLTestRunner

result = '1'
# 4.定义测试类，父类为unittest.TestCase。
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法。
class Test(unittest.TestCase):
    # 5.定义setUp()方法用于测试用例执行前的初始化工作。
    # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    # 注意，输入的值为字符型的需要转为int型

    def setUp(self):
        pass
        # self.number = input('Enter a number:')
        # self.number = int(self.number)



    # 6.定义测试用例，以“test_”开头命名的方法
    # 注意，方法的入参为self
    # 可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    # 可定义多个测试用例

    # 最重要的就是该部分
    def test_001(self):
        global result
        result='2'
        print('test_001执行了,结果是:'+result)

    # @unittest.skip('暂时跳过用例3的测试')
    # def test_003(self):
    #     self.assertEqual(self.number, 30, msg='Your input is not 30')

    @unittest.skipIf(result== '2', '跳过')
    def test_002(self):
        print('test_002执行了,结果是:'+result)



    # 7.定义tearDown()方法用于测试用例执行之后的善后工作。
    # 注意，方法的入参为self
    def tearDown(self):
        pass
    # def tearDownClass(cls):
    #     super(Test, cls).tearDownClass()
    #     print('Test over')


# 8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
# if __name__ == '__main__':
#     # 8.1执行测试用例方案一如下：
#     # unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
#     # 执行顺序是命名顺序：先执行test_case1，再执行test_case2
#     # unittest.main()
#     suit = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(Test))
#     with open('../Report/'+'report.htm','wb') as f:
#         HTMLTestRunner(stream=f,title='标题',description='描述').run(suit)

if __name__ == '__main__':
    suit = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(Test))
    unittest.TextTestRunner(verbosity=2).run(suit)