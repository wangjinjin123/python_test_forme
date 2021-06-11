"""
多环境下的接口测试，实现原理：
在请求之前，对请求的url进行替换
1、需要二次封装requests，对请求进行定制化
2、将请求的结构体的url从一个写死的IP地址改为一个（任意的）域名
3、使用一个evn配置文件，存放各个环境的配置信息
4、然后将请求结构体中url替换为‘evn'配置文件中个人选择的url
5、将evn配置文件使用yaml进行管理
"""
import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))

    #对请求进行二次封装,data是一个请求得信息
    def send(self,data:dict):
        data["url"] = str(data["url"]).replace("famliy.quickan.com",self.env["testing-studio"][self.env["default"]])
        r = requests.request(method=data["method"] ,url=data["url"],headers=data["headers"])
        return r

