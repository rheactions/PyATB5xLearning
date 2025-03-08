

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

    link_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    link_element.click()
    # < a
    # href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class ="text-link"
    # data-qa="bericafeqo" >
    # Start a free trial < / a >

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    driver.quit() #closes everything and .close closses current window
