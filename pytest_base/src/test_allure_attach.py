"""
前端自动化测试-截图
场景：
  前端自动化测试经常需要附加图片或者html，在适当得地方，适当得时机截图
解决：
 @allure.attach显示许多不同类型得提供得附件，可以补充测试、步骤或者测试结果
步骤：
---在测试报告中附加网页：
   allure.attach(body(内容),name,attachment_type,extension)
   allure.attach('<head></head><body>首页</body>‘，“这是错误的信息”,allure.attachment_type.HTML)

----在测试报告中附加图片
    allure.attach.file(source,name,attachment_type,extension)
    allure.attach.file(./resource/222.jpg,attachment_type=allure.attachment_type.JPG)
"""

import allure
def test_attach_text():
    attach