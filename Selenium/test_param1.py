import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]
@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236905/step/1"])
def test_go_link(browser, link):
    browser.get(link)
    time.sleep(5)
    input1 = browser.find_element_by_tag_name("textarea")
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))
    time.sleep(3)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(5)
    result = browser.find_element_by_class_name("smart-hints__hint").text
    assert result == "Correct!", print(result)



