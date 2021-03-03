import math
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options) as browser:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    x_element = browser.find_element_by_tag_name('img')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()

    input3 = browser.find_element_by_id('robotsRule')
    input3.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    time.sleep(30)
