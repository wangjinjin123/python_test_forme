"""
序号	断言方法	断言描述
1	assertEqual(arg1, arg2, msg=None)	验证arg1=arg2，不等则fail
2	assertNotEqual(arg1, arg2, msg=None)	验证arg1 != arg2, 相等则fail
3	assertTrue(expr, msg=None)	验证expr是true，如果为false，则fail
4	assertFalse(expr,msg=None)	验证expr是false，如果为true，则fail
5	assertIs(arg1, arg2, msg=None)	验证arg1、arg2是同一个对象，不是则fail
6	assertIsNot(arg1, arg2, msg=None)	验证arg1、arg2不是同一个对象，是则fail
7	assertIsNone(expr, msg=None)	验证expr是None，不是则fail
8	assertIsNotNone(expr, msg=None)	验证expr不是None，是则fail
9	assertIn(arg1, arg2, msg=None)	验证arg1是arg2的子串，不是则fail
10	assertNotIn(arg1, arg2, msg=None)	验证arg1不是arg2的子串，是则fail
11	assertIsInstance(obj, cls, msg=None)	验证obj是cls的实例，不是则fail
12	assertNotIsInstance(obj, cls, msg=None)	验证obj不是cls的实例，是则fail

"""
"""
testsuite 测试套件
创建测试套件：
suite=unittest.TestSuite() 
添加测试用例：
suite.addTest(simple_test('test_add')) 


"""


#被测函数 search1
import unittest


class Search:
    @staticmethod
    def search_fun():
        print("search_fun")
        return True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
        cls.search = Search()

    # def setUp(self) -> None:
    #     print("set up")
    #     self.search = Search()

    def test_search1(self) -> None:
        print("testsearch1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self) -> None:
        print("testsearch2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self) -> None:
        print("testsearch3")
        # search = Search()
        assert True == self.search.search_fun()


    # def tearDown(self) -> None:
    #     print("tear down")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")



class TestSearch1(unittest.TestCase):

    def test_search1(self):
        print("test_search1_class1")

    def setUp(self) -> None:
        print("set up")
        self.search = Search()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 1,"判断 1 == 1") #疑问：为甚需要用self来引用？
        self.assertFalse(1 == 3, "不相等")


    def test_notequal(self):
        print("断言不等")
        self.assertNotEqual(1,2,"判断 1 ！= 2")
        self.assertTrue(1==2, "不相等")

    def tearDown(self) -> None:
        print("tear down")


class TestSearch2(unittest.TestCase):
    def test_search_a(self):
        print("testsearch_a")

if __name__ == '__main__':
    #方法一，执行当前文件中所有的测试用例
    #unittest.main()
    #方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件中
    #创建一个测试套件-->testsuite
    suite = unittest.TestSuite()
    suite.addTest(TestSearch("test_search1"))
    suite.addTest(TestSearch("test_search3"))
    #suite.addTests()
    unittest.TextTestRunner().run(suite)
    #方法三：执行某个测试类.将测试类添加到测试套件中 批量执行测试类  unittest.TestLoader()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)