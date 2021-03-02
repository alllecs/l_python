import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

link = "http://suninjuly.github.io/find_link_text"

with webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options) as browser:
    browser.get(link)
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    l = browser.find_element_by_link_text(text)
    l.click()

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(30)

