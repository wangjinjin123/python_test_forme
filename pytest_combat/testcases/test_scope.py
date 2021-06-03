"""
定义：
@pytest.fixture()
def fixture_method():
    print("setup")
    yield 返回值
    print("teardown")

调用方法
  测试用例张传入fixture方法名
  @pytest.mark.usefixture("fixture函数名称")
  自动调用 @pytest.fixture(autouse=True)

作用域
   控制方式：@pytest.fixture(scope="")
   scope的取值
      function 默认值
      class
      module
      session

fixture方法返回值的获取

在测试用例中使用fixture方法名可以获取到yield后面的返回值

"""



import pytest

class TestDemo:
    def test_a(self,connectDB):
        print("testcase a")

    def test_b(self):
        print("testcase b")

class TestDemo2:
    def test_a(self):
        print("testcase a")

    def test_b(self):
        print("testcase b")