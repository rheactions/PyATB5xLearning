import pytest
import allure
import requests



@allure.title("verify the Get Request of Restful Booker")
@allure.description("This testcase is for checking the Get response")
@pytest.mark.positive
def test_get_request_positive():
    URL  = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url = URL)
    print(response_data)
    assert response_data.status_code == 200
