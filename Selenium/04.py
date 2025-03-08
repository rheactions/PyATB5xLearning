from selenium import webdriver
import pytest
import allure


@allure.title("Verify that the title pf vwo.com is expected")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service9" in driver.page_source:
        print("test case passed ")
    else:
        print("test case failed")
        pytest.fail("test not found.") # to fail the test case

        #who is closing the brower here
        #that would be Py interpretor


# for running test cases parallely in two browsers
#pip install pytest-xdist
