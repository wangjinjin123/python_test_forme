"""
Json格式转化
如何使用json？
import json

常用的几种方法：
json.dumps(python_obj):可以将传入的json（数据类型）转换成一个字符串
json。loads(json_string):把字符串转换成json(数据类型)
json.dump()：把json（数据类型）转换成字符串并存储在文件中
json.load(file_stream)：把文件打开把里边的字符串抓换成json（数据类型）
"""
import json
data = {
    "name":["herry","niackname"],
    "age": 20,
    "gender":"female"
}

data_1 = json.dumps(data)

print(type(data))
print(type(data_1))
print(data)

data_2 = json.loads(data_1)
print(type(data_2))