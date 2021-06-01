import pytest
import yaml
from decimal import Decimal


class TestCalc:
    @pytest.mark.first
    def test_add(self,get_calc,get_datas_add,all_start):
        result = None
        try:
            #用fixture方法名返回计算器实例并调用计算器中的方法add
            result = get_calc.add(get_datas_add[0], get_datas_add[1])
            if isinstance(result,float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_datas_add[2]

    @pytest.mark.fourth
    def test_div(self,get_calc,get_datas_div):
        result = None
        try:
            result = get_calc.div(get_datas_div[0], get_datas_div[1])
        except Exception as e_div:
            print("division by zero")

        assert result == get_datas_div[2]

    @pytest.mark.second
    def test_sub(self,get_calc,get_datas_sub):
        result = None
        try:
            result = get_calc.sub(get_datas_sub[0],get_datas_sub[1])
            if isinstance(result,float):
                result = round(result, 2)
        except Exception as e_sub:
            print(e_sub)

        assert result == get_datas_sub[2]

    @pytest.mark.third
    def test_mul(self,get_calc,get_datas_mul):
        result = None
        try:
            result = get_calc.mul(get_datas_mul[0],get_datas_mul[1])
            if isinstance(result,float):
                result = round(result, 2)
        except Exception as e_mul:
            print(e_mul)
        assert result == get_datas_mul[2]