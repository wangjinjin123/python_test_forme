"""
python的错误与异常
语法错误与定位
异常捕获、异常处理
自定义异常
"""
"""
异常既是一个事件

"""
try:
    num1 = int(input("请输入一个被除数"))
    num2 = int(input("请输入一个除数"))
    print(num1/num2)
except:
    print("程序出现异常了")

# except ZeroDivisionError:
#     print("除数不能为0噢")
# except ValueError:
#     print("只能输入数值型的整数")
# else:
#     print("没有异常噢~很棒！")
finally:
    print("这个流程已经走完了噢")


#手动抛出的异常
# a = 5
# if a < 10:
#     raise Exception("这是一个手动抛出的异常")


#自定义异常
class MyException(Exception):
    def __int__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

raise MyException("value1", "value2")
