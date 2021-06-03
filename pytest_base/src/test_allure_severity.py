import allure
import pytest


def test_with_no_severity_label():
    pass
@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    print("用例等级是trivial")
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    print("用例等级是normal")
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity:
    def test_inside_the_normal_severity_test_class(self):
        print("inside the normal class")
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        print("the_normal_severity_test_class_with_overriding_critical_severity")
        pass

if __name__ == '__main__':
        pytest.main()

