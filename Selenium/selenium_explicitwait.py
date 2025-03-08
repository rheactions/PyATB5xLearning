import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("App.vwo.com implicit/explicit Wait")
@allure.description("Verificcation that app.vwo.com is loaded with waits")
def test_negative_app_vwo_com():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    #driver.implicitly_waits(5)

    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    pass_web_element = driver.find_element(By.ID,"login-password")
    pass_web_element.send_keys("password@1234")

    submit_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_web_element.click()

    #wait for the error message
    # you should wrap the locatot in the tuple that is just add extra brackets around it
    WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))

    #error_msg = driver.find_element(By.CLASS_NAME,"notification-box-description")
    #print(error_msg.text)

    assert driver.find_element(By.CLASS_NAME,"notification-box-description").text == "Your email, password, IP address or location did not match"

