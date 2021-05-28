"""
结构化请求体构造JSON XML
JSON请求体构造
 payload={‘some’：‘data’}
 r = request.post(url,json=payload)
 
 
 XML请求体构造


 复杂数据解析 mustache
 
 schema校验
 https://jsonschema.net/
 生成schema文件
 根据需要添加自定义规则
"""


import requests
class TestDemo:
    def test_post_json(self):
        payload = {'some': 'data'}
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code == 200
        assert r.json()['json']['some'] == "data"