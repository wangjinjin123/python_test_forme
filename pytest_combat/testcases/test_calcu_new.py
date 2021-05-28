import pytest
import yaml



class TestCalc:

    def test_add(self,get_calc,get_datas):
        result = None
        try:
            #用fixture方法名返回计算器实例并调用计算器中的方法add
            result = get_calc.add(get_datas[0], get_datas[1])
            if isinstance(result,float):
                result = round(result, 2)
        except Exception as e:
            print(e)


        assert result == get_datas[2]



