from selenium import webdriver
from time import sleep
import math

with webdriver.Chrome() as browser:
    #browser.execute_script("alert('Robots at work');")
    #browser.execute_script("document.title='Script executing';")
    #browser.execute_script('document.title="Script executing";')
    #browser.execute_script("document.title='Script executing';alert('Robots at work');")
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    result = math.log(abs(12 * math.sin(int(x))))
    browser.execute_script("window.scrollBy(0, 100);")
    line = browser.find_element_by_id("answer")
    line.send_keys(str(result))
    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()

    input3 = browser.find_element_by_id('robotsRule')
    input3.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




    #button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button) #scroll browser
    #browser.execute_script("window.scrollBy(0, 100);") #scroll 100 pixels
    #button = document.getElementsByTagName("button")[0];
    #button.scrollIntoView(true);
    #button.click()
    sleep(20)
    assert True