"""
使用allure生成测试报告
1、安装allure-pytest插件
pip install allure-pytest
2、运行
  在测试执行期间搜集结果
    pytest [测试文件] -s -q --alluredir=./result/(--alluredir这个选项用于指定存储测试结果的路径)
  查看测试报告
    方式一、测试完成后查看实时报告，在线看报告，会直接打开默认浏览器展示当前报告
        allure serve ./result/(注意：这里的serve得书写)
    方式二、从结果生成报告，这是一个启动tomacat得读物，需要两个步骤：生成报告、打开报告
       生成报告：
         allure generate ./result/ -o ./report/ --clean(注意：覆盖路径加--clean)
        打开报告：
           allure open -h 127.0.0.1 -p 8883 ./report/
执行测试用例并把测试结果指定至某个路径下
$pytest --alluredir=/tmp/my_allure_results
生成测试报告（html）。线上实时查看
$ allure serve /tmp/my_allure_results
"""


import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


