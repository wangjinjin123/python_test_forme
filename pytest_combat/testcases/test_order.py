import pytest


@pytest.mark.run(order=2)
def test_a():
    print("case 1")

@pytest.mark.run(order=3)
def test_b():
    print("case 2")

@pytest.mark.run(order=1)
def test_c():
    print("case 3")


