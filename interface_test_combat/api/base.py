#创建基础类，封装基础api
import requests


class Base:
    #封装请求（包含4种请求方法）
    def __init__(self):
        # 获取通讯录得token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwec359d0349cb57a1&corpsecret=JzhIasSlUFfz81kPlM-m1-qwSbG2JH4hQiZ1r6_2TqQ"
        r = requests.get(url).json()
        # res = requests.get(url)
        self.token = r['access_token']

        #创建session连接，实现其余步骤免token操作
        #声明一个Session
        self.s = requests.session()

        #将查询参数放入params种
        #把token放入session中，每次参数都有token
        self.s.params = {'access_token':self.token}# 也可以往headers中塞cookie等

    #*args:接收位置参数  **kwargs：接收关键字参数
    def send(self,*args,**kwargs):
        #r = requests.request(*args, **kwargs)
        #用session
        r = self.s.request(*args, **kwargs)
        return r.json()


