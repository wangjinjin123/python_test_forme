import pytest
"""
通过fixture也可以实现参数化，不同的fixture传入测试用例中动态生成测试用例
"""

@pytest.fixture(params=[1,2,3],ids=['r1', 'r2', 'r3'])
def login1(request):
    data = request.param
    print("获取测试数据")
    return data + 4
    pass

def test_case1(login1):
    #获取data数据
    print(login1)
    print("测试用例1")
