from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

with webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options) as browser:
#    link = "http://suninjuly.github.io/registration1.html" #not bugs
    link = "http://suninjuly.github.io/registration2.html" #bugs
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block div.first_class input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block div.second_class input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block div input.third")
    input3.send_keys("vano@m.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)
