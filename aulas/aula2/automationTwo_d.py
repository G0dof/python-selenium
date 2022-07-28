import 
from pprint import pprint
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def getLinks(browser, tag):
    result = {}
    element = browser.find_element(By.TAG_NAME, tag)
    anchorElements = element.find_elements(By.TAG_NAME, "a")

    for value in anchorElements:
        result[value.text] = value.get_attribute("href")

    return result

#options = webdriver.EdgeOptions()
# options.add_argument("--headless")
browser = webdriver.Edge()
browser.maximize_window()

URL = "http://selenium.dunossauro.live/aula_04.html"
browser.get(URL)

browser.implicitly_wait(10)

""" 
classes = {}

asideAnchorList = browser.find_elements("xpath", "//aside/ul/li/a")
mainAnchorList = browser.find_elements("xpath", "//main/ul/li/a")

for index, value in enumerate(asideAnchorList):
    classes[value.text] = value.get_attribute("href")

for index, value in enumerate(mainAnchorList):
    if "exercício 3" in value.text.lower():
        value.click()
        break
"""

aulas = getLinks(browser, "aside")
exercicios = getLinks(browser, "main")

pprint(aulas)
pprint(exercicios)
browser.get(exercicios["Exercício 3"])

browser.quit()
