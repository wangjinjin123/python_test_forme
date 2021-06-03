"""
header的构造：
--普通的header：
----headers = {‘user-agent’：‘my-app/0.0.1)
----r = request.get(url,headers=headers)

--cookie
---cookies = dict(cookies_are='working')
----r = requests.get(url,cookies=cookies)


"""
import requests

class Test_Demo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        print(r.request)
        assert r.status_code == 200


    #get quary请求
    def test_quary(self):
        payload={
            "a":1,
             "name":"Lucy"
        }
        r = requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200


    #form请求，常见一些表单,,常见登陆用户名和密码
    def test_form(self):
        payload = {
            "level": 1,
            "name": "lily"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    #文件上传
    def test_fileupload(self):
        file = {'file':open('D:\pycharm\pythonproject\empty_book.xlsx','rb')}
        r = requests.post('https://httpbin.testing-studio.com/post',files=file)
        print(r.text)
        assert r.status_code == 200


    def test_heaser(self):
        r = requests.get("https://httpbin.testing-studio.com/get",headers={"h":"header demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        print(r.headers)
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header demo"


"""
响应结果
基本信息：r.url、r.status_code、r.headers、r.cookies
响应结果：
 r.text=r.encoding+r.content
 r.json()=r.encoding+r.content+content type json
 r.raw.read(10)
 对用的请求内容：r.request

"""


