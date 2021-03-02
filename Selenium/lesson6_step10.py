from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

with webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options) as browser:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_class_name('first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name('second')
    input2.send_keys("Ivan")
    input3 = browser.find_element_by_class_name('third')
    input3.send_keys("Ivan")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")

    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
