
import allure
import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@allure.title("windows handle")
@allure.description("Verify switching to new window")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")

    driver.find_element(By.XPATH,"//a[contains(text(),'Click Here')]").click()
    time.sleep(2)

    
