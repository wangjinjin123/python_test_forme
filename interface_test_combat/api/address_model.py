#建立通讯录类，一套可维护得面向对象的东西
# 通讯录联系人的公共api类
import json

import requests

from interface_test_combat.api.base import Base


class Address(Base):
    # url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwec359d0349cb57a1&corpsecret=JzhIasSlUFfz81kPlM-m1-qwSbG2JH4hQiZ1r6_2TqQ"
    # r = requests.get(url)
    # token = r.json()['access_token']
    # def __init__(self):
    #     # 获取通讯录得token
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwec359d0349cb57a1&corpsecret=JzhIasSlUFfz81kPlM-m1-qwSbG2JH4hQiZ1r6_2TqQ"
    #     r = self.send("get",url)
    #     #res = requests.get(url)
    #     self.token = r['access_token']


    def __init__(self):
        Base.__init__(self)


    def add_user(self, userid:str, name:str, mobile:str, department:list, **kwargs):
        """
               增加联系人，这里代码没有封装，看起来很乱
               :param token: token值
               :param userid: 请求参数的值
               :param name: 请求参数的值
               :param mobile: 请求参数的值
               :return: 返回响应体
               """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            #"alias": "Judy",
            "mobile": mobile,
            "department": department,
        }
        #将kwargs更新到body中
        body.update(kwargs)
        r = self.send("post", url,json=body)
        #r = requests.post(url, json=body)
        return r

    def dele_user(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        r = self.send("get", url)
        #r = requests.get(url)
        return r

    def updata_user(self,userid,name,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name,
        }
        body.update(kwargs)

        header = {'content-type': "application/json"}
        r = self.send("post", url, data = json.dump(body), headers=header)
        #r = requests.post(url, data=json.dumps(body), headers=header)
        return r

    def get_user(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        r = self.send("get", url)
        #r = requests.get(url)
        return r




