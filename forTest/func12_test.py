"""
第三方库
pytest
request

pypi.org 可搜索第三方库说明文档并了解
"""
import requests
res = requests.get("http://www.baidu.com")
print(res.status_code)
print(res.text)

payload = {'key1': 'value1', 'key2': 'value2'}

res1 = requests.post("http://httpbin.org/post", data=payload)
print(res1.text)
