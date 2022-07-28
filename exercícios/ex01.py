from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

URL = "http://curso-python-selenium.netlify.app/exercicio_01.html"

browser.get(URL)

# Delay no código para o carregamento da página - IMPORTANTÍSSIMO
browser.implicitly_wait(10)

headerTag = browser.find_element(By.TAG_NAME, "h1").tag_name
paragraphList = browser.find_elements(By.TAG_NAME, "p")

dictionary = {}
dictionary[headerTag] = {}
for c in range(0, len(paragraphList)):
    dictionary[headerTag][paragraphList[c].get_attribute("atributo")] = paragraphList[c].text

browser.quit()

print(dictionary)