import allure
import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@allure.title("Radio-checkbox")
@allure.description("Verify clicking on radio and checkboxes")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    driver.find_element(By.XPATH,"//input[@id='sex-1']").click()
    driver.find_element(By.XPATH, "//input[@id='profession-1']").click()

    time.sleep(2)