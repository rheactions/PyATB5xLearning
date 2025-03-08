from selenium import webdriver
import pytest
import allure
import time
# we are importing time here cuz we want to see
#the opening and closing of the browsers , here they are getting closed immediately



@allure.title("Verify that the title of katalon.com is expected")
def test_katalon_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    #driver.close() # will close the current window
    driver.quit() # full browser will close 


# for running parallely we use this command
#pytest -n auto -s file path from content root

