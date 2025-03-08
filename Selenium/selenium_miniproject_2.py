

from selenium import webdriver
#import pytest
#import allure
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options



def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    # Use CSS_SELECTOR to select the button with the correct classes
    #link_element = driver.find_element(By.XPATH, "//button[@data-qa='dobevozose']")
    #link_element = driver.find_element(By.CSS_SELECTOR, ".btn.btn--link.btn--primary.Td\\28 u\\29")
    links = driver.find_elements(By.TAG_NAME,"button")
    #you could use the same by replacing a to button for knowing all e buttons on the web page
    for link in links:
        #print(link.get_attribute('href')) # this link.get_attribute is extracting the link itself
        #but you want to extract just the link text then you should use.text
        print(link.text)

# EscapingSpecial Characters in the CSSSelector:
# If the class Td(u) is valid but contains special characters,
# it might need to be properly escaped in a CSS selector.
# This might not be necessary for simple classes,
# but in some cases, you can try escaping the parentheses.

# python Copy Edit
# link_element = driver.find_element(By.CSS_SELECTOR, ".btn.btn--link.btn--primary.Td\\28 u\\29")
# Here, the parentheses( and ) are escaped as  \\28 and \\29, respectively, which is the
# correct way to represent them in a CSSselector.

    # Click the element
    #link_element.click()

    time.sleep(2)
    driver.quit()