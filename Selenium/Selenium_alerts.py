from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Working with different types of alerts")
@allure.description("Handling the JS alerts ")
def test_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_ele = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    alert_ele.click()
    WebDriverWait(driver,3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    result_text = driver.find_element(By.XPATH,"//p[@id='result']").text

    assert result_text == 'You successfully clicked an alert'
