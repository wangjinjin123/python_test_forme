"""
python常用的标准库
操作系统相关：os
时间和日期相关：time datetime
科学技术相关：math
网路请求：urllib
"""

import os
import time
import urllib.request
import math

# # os.makedirs("testdir")
# print(os.listdir("./"))
# #os.removedirs("testdir")
# #获取当前路径
# print(os.getcwd())
#

#在文件夹b中创建一个test.txt文件
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.makedirs("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt", "w")
    f.write("hello,os using")
    f.close()
# g = open("b/test.txt","w")
# g.write("wahaha"/n)
# g.close()


"""
获取当前时间以及时间格式经的模块
导入方式：import time
time模块常用的方法
1、time.asctime() 国外的时间格式
2、time.time() 时间戳
3、time.sleep() 等待
4、time.localtime() 时间戳转换成时间元组
5、 time.strftime() 将当前的时间戳转成带格式的时间
 格式：time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
"""

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H: %M: %S", time.localtime()))
# print(time.strftime("%Y-%m-%d %H: %M: %S"))

#获取2天前现在的时间
# now_timestamp = time.time()
# two_day_before = now_timestamp - 60*60*24*2
# time_tumple = time.localtime(two_day_before)
# print(time.strftime("%Y-%m-%d %H: %M: %S", time_tumple))



"""
urllib库
python------import urllib2
response=urllib2.urlopen("url地址")
python------import urllib。request
response=urllib.request.urlopen("url地址")
"""

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.read())
# print(response.headers)


"""
math库
math.ceil(x) 返回大于等于参数x的最小整数
math.floor(x) 返回小于等于参数x的最大整数
math.sqrt(x) 平方根
"""
print(math.ceil(5.5))
print(math.floor(5.5))
print(math.sqrt(9))




