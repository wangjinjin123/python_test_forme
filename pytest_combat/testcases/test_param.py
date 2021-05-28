import pytest
import yaml


#封装需要用到的数据
def get_datas():
    with open("D:\pycharm\pythonproject\pytest_combat\data\data.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myids"]
        return [add_datas,add_ids]


def add_func(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected",get_datas()[0],ids= get_datas()[1])
def test_add(a,b,expected):
    print(a)
    print(b)
    assert add_func(a,b) == expected



#参数可以组合堆叠使用
@pytest.mark.parametrize(("a"),[1,2,3],ids=["a","b","c"])
@pytest.mark.parametrize(("b"),[1,2,3],ids=["a1","b1","c1"])
def test_foo(a,b):
    print("测试参数堆叠组合：a->%s,b->%s" %(a,b))
    print(f"测试参数堆叠组合：{a},{b}")