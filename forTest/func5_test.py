"""

python输入和输出
字面量打印和格式化
文件读取
Json格式转换
"""


"""
字面量（literal）是以变量或常量给出的原始数据。在程序中可以直接使用字面量
字面量的类型：
数值型
字符型
布尔型
字面量集合：列表  集合 元组 字典
特殊字面量：None
"""



"""
字面量插值
字面量插值就是将变量、常量以及表达式插入的一种技术，它可以避免字符串拼接的问题，很多余元都支持了此功能
字面量插值方法：
1、格式化输出
2、通过string.format()方法拼接
Formatted string literals，字符串格式化机制（>python 3.6）

"""

"""
格式化输出
%的用法
%s :使用str()函数将表达式转换为字符串
%d、%i :转化为带符号的十进制整数
%f /%F:转化为十进制浮点数
"""

age = 3
name = "Lucy"

print('%s,my age is %d' %(name,age))

print('%s,my age is %d, my number is %f' %(name,age,3.1415926))

print('%s,my age is %d, my number is %f' %(name,age,3.14159))

print('%s,my age is %d, my number is %.3f' %(name,age,3.14159))



"""
format()方法
用法：str.format()可将
字符串 print("we are the {} and {} ".format('Tom', 'Jerry'))
列表 print("we are the {0} and {1}".format(*listdata))
字典 print("my name is {name},age is {age}".format(**dictdata))
"""
name1 = 'Lily'
age1 = 20
print('my name is {}, age is {}'.format(name1, age1))
print('my name is {0}, age is {1} ,{0}{1}'.format(name1, age1))

list = ["a",2,3,4]
dict = {"name": "jim", "gender": "male"}
print("my list is {0}, dict is {1}".format(list, dict))
namelist = ["hali", "jerry", "alex"]
#加*相当于给列表解包，拆分成3个
print("we name is : {} 、 {} and {}".format(*namelist))

print("my name is {name}, gender is {gender}".format(**dict))

"""
F-strings:字符串格式化机制 python 3.6以上
使用方法：f'{变量名}，'
注意：
大括号里面可以是表达式或者函数
大括号内不能转义，不能使用‘\’
"""

print(f"my name is {name1}, age is {age1}")
print(f"my name is {name1.upper()}, age is {age1}")
print(f"result is {(lambda x:x+1)(2)}")
print(f"result is {11}")







