from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

URL = "http://selenium.dunossauro.live/aula_04_a.html"

browser.get(URL)

""" 
-- FORMA 1

unorderedList = browser.find_element(By.TAG_NAME, "ul")
listItems = unorderedList.find_elements(By.TAG_NAME, "li")

for counter, value in enumerate(listItems):
    print(value.find_element(By.TAG_NAME, "a").text)

-- FORMA 2

elementList = browser.find_elements("xpath", "//ul[]/li")

for counter, value in enumerate(elementList):
    print(value.text)

-- FORMA 3

def find_element_by_text (browser, tag, text):
    elements = browser.find_elements(By.TAG_NAME, tag)
    for element in elements:
        if element.text == text:
            return element

def find_element_by_href (browser, link):
    elements = browser.find_elements(By.TAG_NAME, "a")
    for element in elements:
        if link in element.get_attribute("href"):
            return element

findDuck = find_element_by_text(browser, "a", "DuckDuckGo")
findReference = find_element_by_href(browser, "google")
"""

browser.quit()
