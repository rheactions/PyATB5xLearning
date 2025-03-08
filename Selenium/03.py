from selenium import webdriver
import pytest
import allure


@allure.title("Verify that the title pf vwo.com is expected")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"




