from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    input_line = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_line.send_keys(calc(x))
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])
    #sleep(20)