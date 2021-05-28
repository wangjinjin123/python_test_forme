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
import yaml
import os

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




#通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "\data.yaml"
print(yaml_file_path)
with open(yaml_file_path) as f:
    data = yaml.safe_load(f)
    print(data)
    datas = data["datas"]
    ids = data["myids"]

#获取yaml文件中得数据并传递给创建得获取数据得fixture方法作为参数，实现参数化
@pytest.fixture(params=datas,ids=ids)
def get_datas(request):
    print("开始计算")
    data_1 = request.param
    print(f"request.param得测试数据是：{data_1}")
    yield data_1  #返回传入的参数
    print("结束计算")