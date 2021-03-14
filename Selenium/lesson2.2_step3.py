from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/selects1.html"

    browser.get(link)

    value1 = browser.find_element_by_id("num1").text
    value2 = browser.find_element_by_id("num2").text
    x = int(value1) + int(value2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x))
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    sleep(10)


#select.select_by_visible_text("text")
#select.select_by_index(index)

#browser.find_element_by_tag_name("select").click()
#browser.find_element_by_css_selector("option:nth-child(2)").click()
#browser.find_element_by_css_selector("[value='1']").click()