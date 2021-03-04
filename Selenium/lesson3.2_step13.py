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
    time.sleep(2)
    return browser.find_element_by_tag_name("h1")

class TestReg(unittest.TestCase):
    def test_link1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        self.assertEqual("Congratulations! You have successfully registered!", go_browser(link1), "It's work!")

    def test_link2(self):
        link2 = "http://suninjuly.github.io/registration2.html" #bugs
        self.assertEqual("Congratulations! You have successfully registered!", go_browser(link2), "There is the bug,",
                                                                                                  " good!")

if __name__ == "__main__": unittest.main()