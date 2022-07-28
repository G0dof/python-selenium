from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

URL = "http://selenium.dunossauro.live/aula_05_b.html"

browser.get(URL)
browser.implicitly_wait(10)

topico = browser.find_element(By.CLASS_NAME, "topico").text
linguagens = browser.find_elements(By.CLASS_NAME, "linguagens")

print(topico)
for linguagem in linguagens:
    print(
        (linguagem.find_element(By.TAG_NAME, "h2").text,
        linguagem.find_element(By.TAG_NAME, "p").text,)
    )

#browser.quit()
