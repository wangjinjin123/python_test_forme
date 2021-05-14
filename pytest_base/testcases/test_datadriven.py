"""
应用场景：
基于测试步骤的数据驱动
基于测试数据的数据驱动
基于配置的数据驱动：切换环境host 和 url地址时使用
"""
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("D:\pycharm\pythonproject\pytest_base\data\evn.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print(env)
            print("测试环境的ip是：",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip是：", env["test"])

