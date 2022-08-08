from time import sleep
from json import loads
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def fillForm(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, "nome").send_keys(nome)
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "senha").send_keys(senha)
    browser.find_element(By.NAME, "telefone").send_keys(telefone)
    browser.find_element(By.NAME, "btn").click()

structure = {
    "nome": "Maria",
    "email": "maria.pereira@uol.com.br",
    "senha": "flor1234",
    "telefone": "(51)956210864"
}
options = webdriver.EdgeOptions()
#options.add_argument("--headless")
browser = webdriver.Edge()
browser.maximize_window()

URL = "http://selenium.dunossauro.live/exercicio_04.html"
browser.get(URL)
browser.implicitly_wait(10)

fillForm(browser, **structure)

sleep(2)

result = loads(browser.find_element(By.TAG_NAME,"textarea").text.replace("\'", "\""))

assert structure == result

browser.close()