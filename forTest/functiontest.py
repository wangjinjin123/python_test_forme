"""
函数代码块以def 关键字开头，后接函数名称和圆括号（）。
冒号起始
注意缩进
圆括号中定义参数
函数说明--文档字符串
return 【表达式】 结束函数
选择性的返回一个值给调用方
不带表达式的return 或者不写return函数，相当于返回None

函数的调用形式
调用时的传参
位置参数
"""
#函数的定义
#位置参数

def func1(a, b, c):
    """
    函数func1的作用
    :param a:参数a用来打印
    :param b:
    :param c:
    :return:
    """
    print("这是一个函数")
    #pycharm快捷键 ctrl + d  复制一行代码
    print("打印出变量a", a)
    print("打印出变量b", b)
    print("打印出变量c", c)
    return a
#函数的调用
print(func1(1, 2, 3))