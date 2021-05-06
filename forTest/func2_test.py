"""
列表的特性
list.append(x)：在列表的末尾添加一个元素，相当于a[len(a)] = [x]
list.insert(i,x):在给定的位置插入一个元素，第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append(x)
list.remove(x):移除列表中第一个值为x的元素，如果没有这样的元素，则抛出ValueError异常
list.pop([i])：删除列表中给定位置的元素并返回她，如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素
list.sort(key=None,reverse=False)：对列表中的元素进行排序（参数可用于自定义排序，解释请参见sorted()
list.reverse():反转列表中的元素
"""

# list_test = [3,4,5]
# list_test.append(1)
# list_test.insert(1,2)
# list_test.remove(1)
# y = list_test.pop()
# print(y)
# list_test.sort()
# list_test.sort(reverse=True)
# list_test.reverse()
# print (list_test)

"""
list.clear()：删除列表中所有的元素，相当于del a[:]
list.extend(iterable)：使用可以迭代对象中的所有元素来扩展列表，相当于a[len(a):] = iterable
list.index(x[,start[,end]]):返回列表中第一个值为x的元素的从零开始的索引。如果没有这样的元素将会抛出ValueError异常
可选参数start和end是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是start参数
list.count(x):返回元素x在列表中出现的次数
list.copy():返回列表的一个浅拷贝，相当于a[:]
注意：
insert、remove或者 sort方法，只修改列表，没有打印处返回值---他们返回默认值None  这是python中所有可变数据结构的设计原则
并非所有的数据或可排序或比较（字符串和数字等）
"""



"""
列表推导式：
概念：列表推导式提供了一哥更简单的创建列表的方法。常见的用法是把某种操作应用于序列或可迭代对象的每个元素上，然后使用其结果来创建列表，或者通过满足某些特定条件元素来创建子序列

练习题：
如果我们想生成一个平方列表，比如[1,4,9.....],使用for循环怎么写？  使用列表推导式又怎么写？
"""

#使用for循环创建平方列表
list_square = []
for i in range(1,4):
    list_square.append(i**2)
print("list_square", list_square)


#使用列表推导式生成列表,本质还是执行一个for循环
list_square2 = [i**2 for i in range(1,4)]
print("list_square2" ,list_square2)


#加入条件判断
list_square3 = []
for i in range(1,4):
    if i!=1:
        list_square3.append(i**2)
print("list_square3", list_square3)



list_square6 = [i**2 for i in range(1,4) if i != 1]
print("list_square6", list_square6)


list_square4 = [i*j for i in range(1,4) for j in range(1,4)]
print ("list_square4", list_square4)

list_square5 = []
for i in range(1,4):
    for j in range(1,4):
        list_square5.append(i*j)
print("list_squares", list_square5)



