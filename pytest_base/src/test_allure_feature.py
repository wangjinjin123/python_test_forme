"""
allure常用特性：

@allure.feature和@allure.story得关系：类似父与子得关系
feature相当于testsuite
story相当于testcase


allure-step
在app、web测试中，最好是每切换到一个新的页面当作一个step
用法：
--@allure.step()，以装饰器得形式放在类或者方法上面
--with allure.step()可以放在测试用例得方法里，但是测试步骤得代码需要被该语句包含




allure特性
"""

import allure


@allure.feature('登陆测试')
class TestLogin():
    @allure.story('登陆成功')
    def test_login_success(self):
        print("这是登陆： 测试用例，  登陆成功")
        pass

    @allure.story('登陆成功')
    def test_login_success_a(self):
        print("这是登陆，测试用例， 登陆失败")
        pass

    @allure.story('用户名缺失')
    def test_login_success_b(self):
        print("用户名缺失")
        pass

    @allure.story('登陆过程之密码丢失')
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("请输入用户名")
        with allure.step("点击用户密码"):
            print("请输入用户密码")
        print("点击登录")
        with allure.step("点击登录后登陆失败"):
            print("登陆失败")
        pass

    @allure.story('登陆失败')
    def test_login_ailure(self):
        print("这是登陆，测试用例， 登陆失败")