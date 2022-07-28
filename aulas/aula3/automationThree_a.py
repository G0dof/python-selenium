from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

URL = "http://selenium.dunossauro.live/aula_05_a.html"

browser.get(URL)
browser.implicitly_wait(10)

divPy = browser.find_element(By.ID, "python")
divHk = browser.find_element(By.ID, "haskell")
print(divHk.text)

browser.quit()
