from selenium import webdriver
#import pytest
#import allure
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options


def test_webtables():
    driver = webdriver.Chrome()
    #driver.get("https://awesomeqa.com/webtable.html")
    driver.get("https://awesomeqa.com/webtable1.html")
    #driver.maximize_window()

    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for col in cols:
            print(col.text)

#find the number of rows using <tbody> , when you count the <tr> tags you'll get to know the number of rows
# now what you'll do is find the xpath for starting from tbody and specify the tr

#row - //table[@id="customers"]/tbody/tr
#column - //table[@id="customers"]/tbody/tr[2]/td

#     row_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
#     row = len(row_elements)
#
#     col_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
#     col = len(col_elements)
#
#     print("Row_length",row)
#     print("Column_length",col)
#
#     first_part = "//table[@id='customers']/tbody/tr["
#     #7 rows - i range(2,i+1)
#     second_part = "]/td["
#     #3 columns - j range(1,3)
#     third_part = "]"
#
#     for i in range(2,row+1):
#         for j in range(1,col+1):
#             dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
#             #print(dynamic_path)
#             #now that we have the xpath of all the cells of table we will find
#             # element with the xpath and then print the text
#             data = driver.find_element(By.XPATH,dynamic_path).text
#             print(data)
#
#
# #in interview they'll ask like find helen bennett and the country she belong sto
#
#             country = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]/following-sibling::td").text
#             if "Helen Bennett" in data:
#                 print(f"Helen belongs to {country}")




