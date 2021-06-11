"""
restful框架
url：每个URI 代表一种资源
交互：客户端和服务器之间，传递这种资源的某种表现层
动作：客户端通过4个http动词/动作（get post delete put）。对服务器端资源进行操作，实现表现层状态转化
表现层含义：资源的呈现形式
资源得含义：网络上的一个实体、文本、图片
状态转化含义：访问网站代表客户端和服务器得互动，post新建资源


实战1作业：
1、利用requests得get 和post实现/封装通讯录得增删改查

"""

import requests

