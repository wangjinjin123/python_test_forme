"""
关联测试用例（可直接给测试用例得地址链接）
关联bug
---执行时需要加个参数
-----allure-link-pattern=issue:http://www.mytesttracker.com/issue.{}

"""


"""
按重要性级别进行一定范围测试
场景：
  通常测试有P0、冒烟测试、验证上线测试。按照重要性级别来分别执行得，iru上线要把主流程和重要模块都跑一遍
  
解决：
  通过附加pytest.mark标记
  通过allure.feature，allure.story
  也可以通过allure.severity来附加标记
      级别：Trivial：不重要， Normal：正常问题， Critical：严重， Blocker：阻塞
步骤：
  在方法、函数、类上面加
     @allure.severity(allure.severity_level.TRIVIAL)
     
    执行时
      pytest -s -v 文件名 --allure-severities normal，critical
"""
import allure


@allure.link("http://www.baidu.com")
def test_with_link():
    print("这是一条添加了链接得测试")
    pass

TEST_CASE_LINK = 'http://www.baidu.com'
@allure.testcase(TEST_CASE_LINK, '测试用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，连接到测试用例里边")
    pass

#--allure-link-pattern=issue:http://www.baidu.com/{}
@allure.issue('140', '这是一个bug')
def test_with_issue_link():
    pass