#文件名统一，放置大家通用的公共模块
#conftest.py文件名是不能变得
#conftest.py与运行得用例要放在同一个package下边
#不需要import导入conftest.py，pytest用例会自动查找
#所有同目录测试文件运行前都会执行conftest.py文件
#全局得配置和前期工作都可以写在这里


"""
场景一：想要创建自己的fixture方法: 遵循就近原则：同文件>同目录>其他目录（也必须是在同一个包下边）
场景二：fixture带参数传递
"""
import pytest
import os

import yaml

from pytest_combat.api.calculator import Calculator
#获取文件所在目录


@pytest.fixture(scope="session")
def connectDB():
    print("链接数据库的操作")
    yield
    print("断开数据库链接")

@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc

@pytest.fixture(scope="module")
def all_start():
    print("开始计算")
    yield
    print("结束计算")

#通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "\data.yaml"
print(yaml_file_path)
with open(yaml_file_path) as f:
    data = yaml.safe_load(f)
    print(data)
    add_datas = data["datas"][:5]
    div_datas = data["datas"][5:8]
    sub_datas = data["datas"][8:11]
    mul_datas = data["datas"][11:]
    ids_add = data["myids"][0:5]
    ids_div = data["myids"][5:8]
    ids_sub = data["myids"][8:11]
    ids_mul = data["myids"][11:]

    print(sub_datas)
    print(mul_datas)
    # ids = data["myids"]

#获取yaml文件中得数据并传递给创建得获取数据得fixture方法作为参数，实现参数化
@pytest.fixture(params=add_datas,ids=ids_add)
def get_datas_add(request):
    # print("开始计算")
    data_1 = request.param
    print(f"request.param得测试数据是：{data_1}")
    yield data_1  #返回传入的参数
    # print("结束计算")


@pytest.fixture(params=div_datas,ids=ids_div)
def get_datas_div(request):
    # print("开始计算")
    data_2 = request.param
    print(f"request.param得测试数据是：{data_2}")
    yield data_2  #返回传入的参数
    # print("结束计算")


@pytest.fixture(params=sub_datas,ids=ids_sub)
def get_datas_sub(request):
    # print("开始计算")
    data_3 = request.param
    print(f"request.param得测试数据是：{data_3}")
    yield data_3  #返回传入的参数
    # print("结束计算")



@pytest.fixture(params=mul_datas,ids=ids_mul)
def get_datas_mul(request):
    # print("开始计算")
    data_4 = request.param
    print(f"request.param得测试数据是：{data_4}")
    yield data_4  #返回传入的参数
    # print("结束计算")