import pytest
import yaml
import sys

from pytest_combat.testcases.test_param import get_datas

print(sys.path)

# sys.path.append("D:\pycharm\pythonproject\pytest_combat\api\calculator.py")

from pytest_combat.api.calculator import Calculator


class TestCal:

    def setup_class(self):
        self.calc = Calculator()


    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("结束计算")





    @pytest.mark.parametrize(("a,b,expected"),get_datas()[0])
    def test_add(self,a,b,expected):
        result = self.calc.add(a,b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected",[(3,2,1),(1,2,-1)])
    def test_sub(self,a,b,expected):
        result1 = self.calc.sub(a,b)
        assert result1 == expected

    @pytest.mark.parametrize(("a, b,expected"),get_datas()[0])
    def test_mul(self,a,b,expected):
        result2 = self.calc.mul(a,b)
        assert result2 == expected

    @pytest.mark.parametrize("a,b,expected",[(3,1,3),(4,2,2)])
    def test_div(self,a,b,expected):
        result3 = self.calc.div(a,b)
        assert result3 == expected






