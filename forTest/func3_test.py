#元组（tuple）使用（）进行定义
#tuple、list、range都是序列数据类型
#元组是不可变的，可以通过解包、索引来访问

#元组的定义
from typing import Set, Any

# tuple_1 = (1,2,3)
# tuple_2 = 1,2,3
# print("tuple_1",tuple_1)
# print("tuple_2",tuple_2)
# print(type(tuple_1))
# print(type(tuple_2))
#
#
# #元组的不可变特性
# list_1 = [1,2,3]
# list_1[1] = 0
# print(list_1)
#
# #执行报错，元组不可变
# # tuple_3 = (1,2,3,4)
# # tuple_3[0] = 0
#
# a = [1,2,3]
# tuple_4 = (4,5,a)
# #打印元组中的指针地址
# print(id(tuple_4[2]))
#
# tuple_4[2][1] = 0
# print("tuple_4",tuple_4)
# print(id(tuple_4[2]))


#元组内置函数
# a = (1,2,3,1)
# print(a.count(1))
# #多个相同的元素则返回首个的角标值
# print(a.index(1))

"""
集合是由不重复元素组成的无序的集合
它的基本用法包括成员检测和消除重复元素
可以使用{}或者set()函数创建集合
要创建一个空集合只能使用set()而不能用{}
"""

# b = set()
# a1 = {1}
# print(len(b))
# print(type(a1))
# print(type(b))

# set_1 = {1, 2, 3}
# set_2 = {3, 4, 5}
# print(set_1)

#求集合的并集
#print(set_1.union(set_2))

#求集合的交集

#print(set_1.intersection(set_2))

#求集合的差集

#print(set_1.difference(set_2))

#添加集合元素
# set_1.add(8)
# print(set_1)

#使用列表推导式创建集合

# set_3 = {i for i in "seaaaeiriehfi"}
# print("set_3",set_3)
#
# #去重
# c = "aabbbeusieut"
# set_4 = set(c)
# print(set_4)



"""
字典是以【关键字】为索引
关键字可以是任意不可变类型，通常是字符串和数字如果一个元组只包含字符串、数字、或元组，那么这个元组也可用作关键字
"""


dict_1 = {}
dict_2 = dict(a=1, b=2)
dict_3 = {"a":1, "b":3, "c":5}
print(dict_1)
print(dict_2)
print(dict_3)

print(type(dict_1))
print(type(dict_2))

#字典的方法
#dict_2.pop("a")
print(dict_2.keys())
print(dict_2.values())

#删除一个key-value对并输出value
# print(dict_2.pop("a"))
# print(dict_2)

#随机删除一个键值对并返回
print(dict_3.popitem())
print(dict_3)

dict_1_1 = dict_1.fromkeys([1,2,3], "a")
print(dict_1_1)


#使用推导式创建字典
dict_4 = {i for i in range(1,4)}
print(dict_4)
