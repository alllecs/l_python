import os
from selenium import webdriver
from time import sleep

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
#file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path)
file_path = os.path.join(current_dir, 'input_file.txt')
with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first = browser.find_element_by_name("firstname")
    first.send_keys("Alex")
    last = browser.find_element_by_name("lastname")
    last.send_keys("Smi")
    email = browser.find_element_by_name("email")
    email.send_keys("A@y.ru")
    f = browser.find_element_by_xpath("//input[@type='file']")
    f.send_keys(file_path)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    sleep(10)