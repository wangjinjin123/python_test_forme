"""
unnitest测试框架
--单元测试覆盖类型：
  --语句覆盖
  --条件覆盖
  --判断覆盖
  --路径覆盖
--框架介绍
  --编写规范
   --测试模块首先import unittest
   --测试类必须继承 unittest.TestCase
   --测试方法必须以“test_”

"""

import unittest

#定义测试类并继承unittest测试类
class TestStringMethods(unittest.TestCase):
    #setUp 和 tearDown 方法是在每条测试用例的前后分别进行调用的方法
    def setUp(self) -> None:#默认返回值是None
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    # setUpCalss 和 tearDownClass 方法是在整个类的前后分别调用的方法
    #类级别的方法需要加一个装饰器:@classmethod
    @classmethod
    def setUpClass(cls) -> None:
        print('set up class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tear down class')

    def test_play(self):
        print('test abc')

    def test_upper(self):
        print('test_upper')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('test_isupper')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('test_split')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#环境准备的测试方法 不应该写在测试用例中

