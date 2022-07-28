from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#options = webdriver.EdgeOptions()
#options.add_argument("--headless")
browser = webdriver.Edge()
browser.maximize_window()

URL = "http://curso-python-selenium.netlify.app/exercicio_02.html"

browser.get(URL)
browser.implicitly_wait(10)

browser.find_element(By.ID, "ancora").click()

correctNumber = (browser.find_elements(By.TAG_NAME, "p")[1].text)[17::]

while True:
    browser.find_element(By.ID, "ancora").click()
    paragraphList = browser.find_elements(By.TAG_NAME, "p")
    if correctNumber in paragraphList[-1].text:
        print(f"O número {correctNumber} foi encontrando, parabéns!")
        break

browser.quit()