from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("--headless")
browser = webdriver.Edge(options=options)

"""
* Cotação - Dólar *

url = "http://google.com.br/"
today = f"{datetime.today().day}/0{datetime.today().month}/{datetime.today().year}"

browser.get(url)
browser.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dolar", Keys().ENTER)
dolar = browser.find_element("xpath", "//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span[1]").get_attribute("data-value")

print(f"A cotação do dólar do dia {today} é {float(dolar):.2f}")
"""

browser.get("http://en.wikipedia.org/wiki/Marvel_Entertainment")
textos = browser.find_elements(By.TAG_NAME, "p")

cont = 0
for i, c in enumerate(textos):
    cont += textos[i].text.lower().count("spider")

print(f"O nome spider foi dito {cont} vezes nos parágrafos deste artigo, muito incrível!")

browser.quit()
