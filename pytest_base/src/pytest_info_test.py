"""
pytest测试框架
测试用例的识别和运行
测试文件：
--test_*.py
--*_test.py

用例识别：
--Test*类包含的所有test_*的方法（重点：测试类中不能带有__init__方法）
--不在class中的所有test_*方法

pytest也可以执行unittest框架写的测试用例和方法
"""
import pytest


def func(x):
    return x + 1
#参数化，重点需要掌握内容
@pytest.mark.parametrize('a,b', [
    (1,2),
    (10,20),
    ('a1', 'a2'),
    (3,4),
    (5,6)
])
def test_answer(a, b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

"""
fixture使用详解：
1、fixture可以当做参数传入

定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()，fixture命名不要以test开头，跟用例区分开。
fixture是有返回值得，没有返回值默认为None。用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。

示例：
@pytest.fixture()
def test_01():
    a = 5
    return a

def test_02(test_01):
    assert test_01 == 5
    print("断言成功")
    
    
2、使用多个fixture

如果用例需要用到多个fixture的返回数据，fixture也可以返回一个元祖，list或字典，然后从里面取出对应数据。    

示例：
@pytest.fixture()
def test_01():
    a = 5
    b = 6
    return (a, b)
 
def test_02(test_01):
    a = test_01[0]
    b = test_01[1]
    assert a < b
    print("断言成功")
    
    
3、fixture的作用范围（scope）

fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function
   -function：每一个函数或方法都会调用
   -class：每一个类调用一次，一个类中可以有多个方法
   -module：每一个.py文件调用一次，该文件内又有多个function和class
   -session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
示例：
@pytest.fixture(scope="class")
def test_01():
    a = 5
    b = 6
    return (a, b)
 
 
class TestNum:
    def test_02(self,test_01):
        a = test_01[0]
        b = test_01[1]
        assert a < b
        print("断言成功")   

"""

@pytest.fixture()
def login():
    username = 'Lily'
    print("登陆结果")
    return username


class TestDemo:
    #
    def test_a(self,login):
        print(f"a username = {login}")

    def test_b(self):
        print("b")

    def test_c(self,login):
        print(f"c username = {login}")


#python解释器运营入口方法
if __name__ == '__main__':
    #实际上是使用pytest解释器执行
    pytest.main(['pytest_info_test.py']) #使用pytest解释器执行全部测试用例 pytets + .py文件
    #pytest.main(['pytest_info_test.py::TestDemo','-v']) #使用python解释器，模仿pytest解释器中的模式   python + .py文件 指定某条测试用例或者某个测试类来执行
    #pytest.main(['pytest_info_test.py','-v'])#python + .py文件




"""
pytest命令参数：
-k: 指定某条测试用例执行   pytest -k + 指定的测试用例的名称
-m:
"""