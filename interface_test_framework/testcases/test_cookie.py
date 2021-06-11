#传递Cookie的两种方式：1、通过请求头信息传递  2、通过请求得关键字参数cookies传递

#通过自定义header传递

import requests

def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {"Cookie": "hogwarts=school",
              'User-Agent': 'wow'}
    r = requests.get(url = url,headers = header)
    print(r.request.headers)


#使用cookies参数传递

def test_demo1():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {'User-Agent': 'wow'}
    cookie_data= {"hogwarts":"school",
                  "people":"teacher"}#需要是一个字典
    r = requests.get(url = url,cookies = cookie_data,headers = header)
    print(r.request.headers)