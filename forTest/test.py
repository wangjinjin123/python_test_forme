"""
分段函数求值
      3x-5 （x>1）
f(x) = x+2 (-1<=x<=1)
        5x +3 (x<-1)
"""
#分支结构
#x = -2
#if x > 1:
#    y = 3*x-5
#elif x < -1:
#    y = 5*x+3
#else:
#    y = x+2
#print(y)

def calculate(x):
    if x > 1:
        y = 3*x-5
    elif x < -1:
        y = 5*x+3
    else:
        y = x+2
    print(y)
calculate(2)





