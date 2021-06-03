import pytest


@pytest.fixture()
def connectDB():
    print("test_demo1 下的 conftest")
def test_a(connectDB):
    print("这是sub_demo中test_a")


class TestB:
    def test_b(self):
        print("这是sub_demo中test_b")