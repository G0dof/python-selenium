from time import sleep
from json import loads
from urllib.parse import urlparse
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.EdgeOptions()
# options.add_argument("--headless")
browser = webdriver.Edge()
browser.maximize_window()

URL = "http://selenium.dunossauro.live/aula_05.html"

browser.get(URL)
browser.implicitly_wait(10)


def fillForm(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, "nome").send_keys(nome)
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "senha").send_keys(senha)
    browser.find_element(By.NAME, "telefone").send_keys(telefone)
    browser.find_element(By.NAME, "btn").click()


structure = {
    "nome": "Leonardo",
    "email": "joquinha123@uol.com",
    "senha": "pipipi123",
    "telefone": "(11)987654321"
}

fillForm(browser, **structure)

sleep(1)

parsedURL = urlparse(browser.current_url)

result = loads(browser.find_element(By.ID, "result").text.replace("\'", "\""))

try:
    assert result == structure
except AssertionError:
    print("Erro")
else:
    print("Sucesso")
finally:
    print("Fim")

browser.quit()
