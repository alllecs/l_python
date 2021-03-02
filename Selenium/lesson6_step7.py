import math
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options) as browser:
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(30)

