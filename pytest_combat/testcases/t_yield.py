#生成器讲解---yield

#yield生成器
def provider():
    #循环读取数据列表
    for i in range(10):
        print("开始操作")
        yield i
        print("结束操作")

p = provider()
for i in p:
    print(i)

# print(p)
# #每次通过next方法只能拿到一个数据
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))