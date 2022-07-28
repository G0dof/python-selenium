from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

URL = "http://selenium.dunossauro.live/aula_04_b.html"

browser.get(URL)
browser.implicitly_wait(10)

analyzedURL = urlparse(browser.current_url)

browser.quit()
