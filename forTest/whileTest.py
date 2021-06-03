#while和else结合使用简单介绍

a=1
while a == 1:
    print("a==1")
    a = a + 1
else:
    print("a != 1")
    print(a)

#简单语句组(若while循环体中只有一个语句，则可和while写在同一行)

a=1
while a == 1:a = a + 1
else:
    print("a != 1")
    print(a)

#break:跳出整个循环体
for i in range(1,10):
    if i == 5:
        break
    print(i)

#continu:跳出当前循环而费整个循环体
for i in range(1,10):
    if i == 5:
        continue
    print(i)
