import unittest


from pytest_base.utill.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    report_title = 'TestSearch用例执行报告'
    desc = '我的第一个测试报告'
    report_file = './result.html'
    #执行方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    test_dir = 'pytest_base/testcases'
    disvcover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    #unittest.TextTestRunner(verbosity=2).run(disvcover)
    with open(report_file ,"wb") as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(disvcover)



"""
测试用例执行过程：
1、写好测试用例
2、由TestLoader加载TestCase到TestSuite
3、由TextTestRunner来运行TestSuite
4、运行的结果保存在TextTestResult中
5、整个过程集成在unittest.main模块中
6、TestCase可以是多个，TestSuite也可以是多个
"""