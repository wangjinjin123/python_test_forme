import pytest



@pytest.mark.second
def test_a():
    print("case 1")


@pytest.mark.last
def test_b():
    print("case 2")

@pytest.mark.first
def test_c():
    print("case 3")

