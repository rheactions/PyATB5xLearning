import allure
import pytest



@allure.title("verify the multiply operator")
@allure.description("This is the test case to check the math multiplication")
@pytest.mark.positive
def test_method2():
    print("this is pytest case")
    assert 1 * 1 == 1


@allure.title("verify the addition operator")
@pytest.mark.positive
def test_method3():
    print("this is pytest case")
    assert 1 + 1 == 2
