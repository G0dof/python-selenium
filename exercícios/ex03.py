from pprint import pprint
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def getLinks(browser, firstTag, secondTag, keyWord=None):
    element = browser.find_element(By.TAG_NAME, firstTag)
    tagList = element.find_elements(By.TAG_NAME, secondTag)

    for value in tagList:
        if keyWord.lower() in value.text.lower():
            value.click()
            break
        if keyWord.lower() in value.get_attribute("attr"):
            value.click()
            break

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)
browser.maximize_window()

URL = "http://selenium.dunossauro.live/exercicio_03.html"
browser.get(URL)

browser.implicitly_wait(10)

getLinks(browser, "main", "a", "começar")
getLinks(browser, "main", "a", "errado")
getLinks(browser, "main", "a", browser.title)
getLinks(browser, "main", "a", urlparse(browser.current_url).path[1::])
browser.refresh()

pprint(browser.find_element(By.TAG_NAME, "pre").text)

browser.quit()
