import json

import requests
#获取通讯录得token
def test_demo():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwec359d0349cb57a1&corpsecret=JzhIasSlUFfz81kPlM-m1-qwSbG2JH4hQiZ1r6_2TqQ"
    r = requests.get(url)
    token = r.json()["access_token"]

    #读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=WangJinJin"
    r = requests.get(url)
    # print(r.json())
    # print(r.json()["errcode"])
    #修改成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
            "userid": "WangJinJin",
            "name": "云沐"
            }
    header = {'content-type' : "application/json"}
    r = requests.post(url, data=json.dumps(body), headers = header)
    print(r.json())
    #添加成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body1 = {
    "userid": "moyuqingfeng",
    "name": "墨雨清风",
    "alias": "Judy",
    "mobile": "13728814530",
    "department": [1]
}
    body2 = {
        "userid": "xiaobai",
        "name": "小白只蠢不萌",
        "alias": "Lily",
        "mobile": "13728814535",
        "department": [1]
    }
    body3 = {
        "userid": "ceshishanchu",
        "name": "删除",
        "alias": "Lucy",
        "mobile": "13728814525",
        "department": [1]
    }
    r1 = requests.post(url, json=body1)
    r2 = requests.post(url, json=body2)
    r3 = requests.post(url, json=body3)

    # print(r1.json())
    # print(r2.json())
    #删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=ceshishanchu"
    r = requests.get(url)
    #print(r.json())

