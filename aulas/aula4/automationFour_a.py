from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
# options.add_argument("--headless")
browser = webdriver.Edge(options=options)
browser.maximize_window()

URL = "https://selenium.dunossauro.live/aula_06_a.html"
browser.get(URL)
browser.implicitly_wait(5)

# browser.close() 
