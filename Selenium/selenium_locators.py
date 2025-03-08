from selenium import webdriver
import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_katalon_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # time.sleep(5)
    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"


    #<a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment</a>

    #2.find the element
    make_appointment_element= driver.find_element(By.ID,"btn-make-appointment")
    #3.click on it
    make_appointment_element.click()
    #4.assert i.e verify the url
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(3)
    driver.quit() #closes everything and .close closses current window
