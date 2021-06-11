# import datetime
# import os
# import time
#
#
# path_1 = os.path.realpath(__file__)
# print(path_1)
# path_2 = os.path.dirname(os.path.realpath(__file__))
# print(path_2)
# BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(BASE_PATH)
#
# print(datetime.date.today())
# log_name = "logs"
#
# a = log_name + "_" + str(datetime.date.today()) + ".log"
# b = os.path.join(BASE_PATH, "logs", a)
# print(a)
# print(b)
import requests

from interface_test_combat.api.address_model import Address

url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwec359d0349cb57a1&corpsecret=JzhIasSlUFfz81kPlM-m1-qwSbG2JH4hQiZ1r6_2TqQ"
r = requests.get(url)
token = r.json()['access_token']
print(token)





url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
body = {
        "userid": "today",
        "name": "今天",
        #"alias": "Judy",
        "mobile": "13728814590",
        "department": [1]
    }
r = requests.post(url, json=body)
print(r.json())


