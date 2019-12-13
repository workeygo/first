# coding=utf-8
import unittest
result = '1'
print('第一个执行 result值是'+result,hash(result))
class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        global result
        result = '2'
        print('第三个执行 result值是'+result,hash(result))

    @unittest.skipIf(result=='2','跳过')
    def test2(self):
        print('第四个执行 result值是'+result,hash(result))

    def tearDown(self):
        pass

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Test("test1"))
    suit.addTest(Test("test2"))
    unittest.TextTestRunner(verbosity=2).run(suit)

    # suit = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(Test))
    # unittest.TextTestRunner(verbosity=2).run(suit)