

import allure
import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



@allure.title("Actions P1")
@allure.description("Verify Actions P1")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.NAME,"firstname")

    actions = ActionChains(driver)

    (actions
     .key_down(Keys.SHIFT)
     .send_keys_to_element(first_name,"arjun")
     .key_up(Keys.SHIFT)
     .perform())


