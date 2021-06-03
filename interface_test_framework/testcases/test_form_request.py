
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
import pystache as pystache
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





"""
请求体复杂时该怎处理一下呢？
数据保存：将复杂的xml或者json请求体保存到文件模板中
数据处理：
  方法一：使用mustache、freemaker等工具解析
  方法二：简单的字符串替换
  方法三：使用json xml api进行结构化解析
  
数据生成：输出最终结果
"""

pystache.render(
    "Hi {{person}}!",
    {'person':'Judy'}
)