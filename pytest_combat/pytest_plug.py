"""
pytest常用插件
pip install pytest-rerunfailures-----失败重跑--有些场景下重要的用例需要重跑，加装饰器
---pytest --reruns 5---指定失败用例重跑次数
---pytest --reruns 5 --reruns-delay 1---指定失败用例重跑次数以及每次重跑间隔时间
pip install pytest-assume------多重校验
---使用场景：一个方法中写有多条断言，中间有一条失败，后边的代码就不执行了；希望有失败也能执行完所有断言
---安装：pip install pytest-assume
---执行：pytest。assume(1==4);pytest.assume(2==4)

pip install pytest-ordering-----控制用例的执行顺序
--场景：对于继承测试，经常会有上下文依赖关系的测试用例
--安装：pip install pytest-ordering
--执行：@pytest.mark.run(order=2)

---case基本设计原则
------不要让case有顺序
-------不要让测试用例有依赖
-------如果无法做到，可以临时性的用插件解决
pip install pytest-xdist----分布式并发执行测试用例
"""

