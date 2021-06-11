# import os
#
# import pytest
# import yaml
#
# from interface_test_combat.api.address_method import Address
# from interface_test_combat.requests_method import HttpRequest
#
#
# @pytest.fixture(scope="session")
# def get_request():
#     print("获取请求方法实例")
#     request_1= HttpRequest()
#     return request_1
#
# @pytest.fixture(scope="class")
# def get_addr():
#     print("获取通讯录方法实例")
#     addr = Address()
#     return addr
#
# @pytest.fixture(scope="class")
# def get_token(get_request):
#     url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwec359d0349cb57a1&corpsecret=JzhIasSlUFfz81kPlM-m1-qwSbG2JH4hQiZ1r6_2TqQ"
#     r = get_request.request(url=url,method="get")
#     token = r.json()["access_token"]
#     return token
#
#
#
# #通过 os.path.dirname 获取当前文件所在目录的路径
# yaml_file_path = os.path.dirname(__file__) + r"\user_data.yaml"
# print(yaml_file_path)
# with open(yaml_file_path,encoding='utf-8') as f:
#     data = yaml.safe_load(f)#读取yaml文件中的数据赋给data变量
#     #print(data)
#     adduser_url = data["address"][0]['url']
#     adduser_data = data["address"][0]['data']
#     adduser_method = data["address"][0]['method']
#
#     deleuser_url = data["address"][1]['url']
#     deleuser_method = data["address"][1]['method']
#
#     updateuser_url = data["address"][2]['url']
#     updateuser_data = data["address"][2]['data']
#     updateuser_method = data["address"][2]['method']
#
#     getuser_url = data["address"][3]['url']
#     getuser_method = data["address"][3]['method']
#
#     # print(adduser_url)
#     # print(adduser_data)
#     # print(adduser_method)
#
# @pytest.fixture(params=[adduser_url,adduser_data,adduser_method])
# def get_adduser_data(request):
#     data_add = []
#     data_add = list(request.param)
#     print(f"request.param得测试数据是：{data_add}")
#     data_add = data_add.append(data_add)
#     yield data_add  # 返回传入的参数
#
# @pytest.fixture(params=[deleuser_url,deleuser_method])
# def get_deleuser_data(request):
#     data_dele = request.param
#     print(f"request.param得测试数据是：{data_dele}")
#     yield data_dele  # 返回传入的参数
#
#
# @pytest.fixture(params=[updateuser_url,updateuser_data,adduser_method])
# def get_updateuser_data(request):
#     data_update = request.param
#     print(f"request.param得测试数据是：{data_update}")
#     yield data_update  # 返回传入的参数
#
# @pytest.fixture(params=[getuser_url,getuser_method])
# def get_getuser_data(request):
#     data_get = request.param
#     print(f"request.param得测试数据是：{data_get}")
#     yield data_get  # 返回传入的参数