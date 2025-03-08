from selenium import webdriver
#import pytest
#import allure
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options



def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn--link.btn--primary")
    button.click()



    time.sleep(2)
    driver.quit()