from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def fillForms(row, column, browser):
    try:
        assert isinstance(row, int) and isinstance(column, int)
    except AssertionError:
        print("\033[1;31mTry again\033m")
        browser.close()
    else:
        nome = browser.find_element(
            By.CSS_SELECTOR, f".form-l{row}c{column} input[name*='nome']")
        senha = browser.find_element(
            By.CSS_SELECTOR, f".form-l{row}c{column} input[name*='senha']")
        btn = browser.find_element(
            By.CSS_SELECTOR, f".form-l{row}c{column} input[type*='submit']")

        nome.send_keys("Pedrinho", )
        sleep(.5)
        senha.send_keys("jorginho213")
        sleep(.5)
        btn.click()
    finally:
        print("\033[1;34mForm filled sucessfully!\033m")

browser = webdriver.Edge()
browser.maximize_window()

URL = "https://selenium.dunossauro.live/exercicio_05.html"
browser.get(URL)
browser.implicitly_wait(5)

fillForms(0, 0, browser)
fillForms(0, 1, browser)
fillForms(1, 0, browser)
fillForms(1, 1, browser)

browser.close()
