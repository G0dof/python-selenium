from urllib.parse import urlparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def find_element_by_text (browser, tag, text):
    elements = browser.find_elements(By.TAG_NAME, tag)
    for element in elements:
        if element.text == text:
            return element

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

URL = "http://selenium.dunossauro.live/aula_04_b.html"

browser.get(URL)
browser.implicitly_wait(10)

boxesName = ["um", "dois", "tres", "quatro"]

for name in boxesName:
    find_element_by_text(browser, "div", name).click()

for name in boxesName:
    browser.back()
    sleep(.3)

for name in boxesName:
    browser.forward()
    sleep(.3)

browser.quit()
