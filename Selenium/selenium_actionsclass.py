import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



@allure.title("Actions P1")
@allure.description("Verify Actions P1")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://chatgpt.com")

    # modal_element = driver.find_element(By.CLASS_NAME,"flex-grow overflow-y-auto")
    # close_modal_element = driver.find_element(By.XPATH,"//a[text()='Stay logged out']")
    #
    #
    # #actions
    # actions = ActionChains(driver)
    #
    # #define the action
    # actions.move_to_element(modal_element).click(close_modal_element).perform()

    modal_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//textarea[@placeholder='Ask anything']"))
    )

    actions = ActionChains(driver)

    actions.move_to_element(modal_element).click().perform()
    time.sleep(1)  # Optional, to allow the page to update, but use explicit waits when possible.
    actions.send_keys("Hi").perform()


