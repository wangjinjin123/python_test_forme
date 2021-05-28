import pytest
#fixture是pytest的一个外壳函数，可以模拟setup和teardown的操作
#yield之前的操作相当于setup，yiel之后的操作相当于teardown
#yield相当于 return，如果需要返回数据，直接放在yield后边
#创建一个登陆的fixture方法
#加上aotouse参数后，默认所有测试用例都调用，如果想要yield有返回值必须在函数中带fixture函数名

@pytest.fixture()
def login():
    print("登陆操作")
    print("获取token")
    username= "tom"
    password = "11111"
    token = "token123"
    #fixture中类似teardown的方式、
    #使用yield返回数据
    yield [username,password,token]
    print("登出操作")


#测试用例1：需要提前登陆

def test_case1(login):
    #想要使用fixture函数中返回的值，则直接在方法中使用fixture方法的名称即可
    print(f"login username and password:{login}")
    print("测试用例1")


#测试用例2：不需要提前登陆
def test_case2(connectDB):
    print("测试用例2")


#测试用例3：需要提前登陆
def test_case3():
    print("测试用例3")

#测试用例4：需要提前登陆
# @pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")