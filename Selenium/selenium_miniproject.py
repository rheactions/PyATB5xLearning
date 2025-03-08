

from selenium import webdriver
import pytest
import allure
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os

@allure.description("VWO Login credentials neg")
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    #url = os.getenv("URL")
    #print(f"URL: {url}")
    #print(f"Environment URL: {os.getenv('URL')}")

    # 1. Find the email and enter the wrong username or email
    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # fdprocessedid="rw1xe" >

    email_element = driver.find_element(By.ID,"login-username")
    email_element.send_keys(os.getenv("INVALID_USERNAME"))

    #< input
    # type = "password"
    # class ="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # fdprocessedid="jf17op" >

    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys(os.getenv("INVALID_PASSWORD"))

#     < button
#     type = "submit"
#     id = "js-login-btn"
#      class ="btn btn--positive
#     btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica" fdprocessedid="76k9gti" >
#
#     < span
#
#     class ="icon loader hidden" data-qa="zuyezasugu" > < / span >
#
#     < span
#     data - qa = "ezazsuguuy" > Sign in < / span >
#
# < / button >

    signin_element = driver.find_element(By.ID, "js-login-btn")
    signin_element.click()
    time.sleep(3)
    # Sometimes, there can
    # be
    # a
    # timing
    # issue
    # with dynamic elements like error messages.After you click the sign- in button, the error message may take some time to appear.To handle this, you should introduce an explicit wait, as mentioned earlier.

    # < div
    # class ="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi" >
    # Your email, password, IP address or
    # location did not match < / div >

    error_web_element = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_web_element.text)

    #assert error_web_element.text == "Your email, password, IP address or location did not match"
    assert error_web_element.text == os.getenv("Error_Message")

    driver.quit() #closes everything and .close closses current window
