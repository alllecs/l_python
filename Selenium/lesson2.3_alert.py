import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    input_line = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_line.send_keys(calc(x))
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])
    sleep(20)