"""
默认参数
默认参数在定义函数的时候使用k=v的形式定义
调用函数时，如果没有传递参数，则会使用默认参数；如果传入了参数则使用传入参数
"""
def func1(a=1):
    print("参数a的值为", a)

func1()
"""
关键字参数
在调用函数的时候，使用k=v的方式进行传参
在函数调用/定义中，关键字参数必须跟随再位置参数的后边
"""

def func1_1(m, n, k, l):
    print("参数m的值为", m)
    print("参数n的值为", n)
    print("参数k的值为", k)
    print("参数l的值为", l)

func1_1(m = 1, l = 2, k = 4, n= 0)


"""
Lambda表达式
可以用lambda关键字来创建一个小的匿名函数
lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda表达式中封装有限的逻辑进去
"""
func1_2 = lambda x : x*2

print(func1_2(3))

#等价于以下函数
def func1_3(x):
    return x*2

print(func1_3(3))


