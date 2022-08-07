from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def fillForm(browser, movie, email, phone):
    browser.find_element(By.NAME, "filme").send_keys(movie)
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "telefone").send_keys(phone)
    browser.find_element(By.NAME, "enviar").click()

#options = webdriver.EdgeOptions()
# options.add_argument("--headless")
browser = webdriver.Edge()

URL = "http://selenium.dunossauro.live/aula_05_c.html"

browser.get(URL)
browser.implicitly_wait(10)

fillForm(browser, "Parasite", "jorgeperes@uol.com.br", "(051)987654321")

#browser.quit()
