import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

link = "http://suninjuly.github.io/find_xpath_form"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
with webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options) as browser:
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
    time.sleep(30)

