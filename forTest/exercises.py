"""
练习题 1、计算1~100求和
      2、加入分支结构实现1~100之间的偶数求和
     3、使用python实现1~100之间的偶数求和
"""
#练习题1
#import random
import random

result = 0
for i in range(101):
    print(i)
    result = result + i
print(result)

#练习题2
result = 0
for i in range(101):
    if(i%2 == 0):
        print(i)
        result = result + i
print(result)

#练习题3
result = 0
for i in range(2, 101, 2):
    print(i)
    result = result + i
print(result)


"""
猜数字游戏
1、计算机出一个1~100之间的随机数由人来猜
2、计算机根据人猜的数字分别
3、给出提示大一点/小一点/猜对了
"""

#随机出一个1~100的数字

computer_number = random.randint(0,100)

print(computer_number)

while True:
    person_number = int(input("请输入一个数字"))
    if person_number > computer_number:
        print("小一点")
    elif person_number < computer_number:
        print("大一点")
    else:
        print("猜对了")
        break

#猜数字游戏封装版

def game_Number(computer_number):
    while True:
        person_number = int(input("请输入一个数字"))
        if computer_number < person_number:
            print("小一点")
        elif computer_number > person_number:
            print("大一点")
        else:
            print("猜对了")
            break
computer_number = random.randint(0, 100)

game_Number(computer_number)




