from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()

URL = "https://selenium.dunossauro.live/exercicio_06.html"
browser.get(URL)
browser.implicitly_wait(5)
sleep(2)

while True:
    fillValidation = browser.find_element(
        By.CSS_SELECTOR, "header p > span#num").text
    if fillValidation == "":
        break
    formRowCol = browser.find_element(By.CSS_SELECTOR, "header p > span").text

    name = browser.find_element(
        By.CSS_SELECTOR, f".form-{formRowCol} input[name='nome']")
    password = browser.find_element(
        By.CSS_SELECTOR, f"form.form-{formRowCol} input[name='senha']")
    btn = browser.find_element(
        By.CSS_SELECTOR, f".form-{formRowCol} input[type='submit']")

    name.send_keys("Jorginho")
    password.send_keys("eusoumuitobonito1234")
    btn.click()

browser.close()
print("\033[1;32mSucessfully finished")
