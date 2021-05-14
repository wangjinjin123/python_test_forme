import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a,b",[(3,4),(20,4),(3,9)])
    def test_data(self,a,b):
        print(a+b)

    @pytest.mark.parametrize(("a","b"), [(3, 4), (20, 4), (3, 9)])
    def test_data(self, a, b):
        print(a + b)\

    @pytest.mark.parametrize(["a","b"],[(3,4),(20,4),(3,9)])
    def test_data(self,a,b):
        print(a+b)


    @pytest.mark.parametrize(("a","b"), yaml.safe_load(open("D:\pycharm\pythonproject\pytest_base\data\data.yaml")))
    def test_data(self, a, b):
        print(a + b)

