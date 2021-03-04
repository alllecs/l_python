import unittest
from selenium import webdriver
import time 

def go_browser(link):
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("div.first_block div.first_class input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block div.second_class input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block div input.third")
    input3.send_keys("vano@m.ru")
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    time.sleep(2)
    return browser.find_element(By.CSS_SELECTOR, "h1").text

class TestReg(unittest.TestCase):
    def test_link1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        result_text = go_browser(link1)
        expected_text = "Congratulations! You have successfully registered! Поздравляем! Вы успешно зарегистировались!"
        assert result_text in expected_text, \
            f"Oops! {expected_text} was expected, got {result_text} instead"

    def test_link2(self):
        link2 = "http://suninjuly.github.io/registration2.html" #bugs
        result_text = go_browser(link2)
        expected_text = "Congratulations! You have successfully registered! Поздравляем! Вы успешно зарегистировались!"
        assert result_text in expected_text, \
            f"Oops! {expected_text} was expected, got {result_text} instead"

if __name__ == "__main__": unittest.main()