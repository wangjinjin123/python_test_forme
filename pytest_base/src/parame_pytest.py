"""
使用参数化功能管理类似用例

1、数据写死在py中
@pytest.mark.parametrize(argnames, argvalues)
--argnames: 要参数化的变量， 可以是：string (逗号分隔)、list、tuple
--argvalues： 参数化的值，list、list[tuple]

argnames和argvalues一定是一一对应的

2、数据存在yaml文件中
list:
- 10
- 20
- 30

dict:
by:id
locator:name
action:click

进行嵌套：
-
  - by：id
  - locator:name
  - action:click

companies:
-
  id:1
  name:company1
  price:200w
-
  id:2
  name:company2
  price:500w

"""
import pytest

#使用sring
@pytest.mark.parametrize("a,b",[(10,20),(20,30)])
def test_param(a,b):
    print(a+b)


#使用list
@pytest.mark.parametrize(['a','b'],[(10,20),(20,30)])
def test_param(a,b):
    print(a+b)
    assert a+b == 50

#使用tuple
@pytest.mark.parametrize(('a','b'),[(10,20),(20,30)])
def test_param(a,b):
    print(a+b)
    assert a+b == 30




