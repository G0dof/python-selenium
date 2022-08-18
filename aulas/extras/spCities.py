from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

URL = "https://www.cidade-brasil.com.br/estado-sao-paulo.html"
browser.get(URL)
cidadesSP = browser.find_elements("xpath", "//div[@class='annuaire']/ul/li")

for cidade in cidadesSP:
    print(f"{cidade.text}\n")

browser.close()
