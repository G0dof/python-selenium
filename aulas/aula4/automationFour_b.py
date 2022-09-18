from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
# options.add_argument("--headless")
browser = webdriver.Edge(options=options)
browser.maximize_window()

URL = "https://selenium.dunossauro.live/aula_06_a.html"
browser.get(URL)
browser.implicitly_wait(5)

# Utilizando atributo type [attr="value"]

# nome = browser.find_element(By.CSS_SELECTOR, "[type='text']")
# senha = browser.find_element(By.CSS_SELECTOR, "[type='password']")
# btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

# Utilizando atributo name [attr="value"]

# nome = browser.find_element(By.CSS_SELECTOR, "[name='nome']")
# senha = browser.find_element(By.CSS_SELECTOR, "[name='senha']")
# btn = browser.find_element(By.CSS_SELECTOR, "[name='l0co0']")

# Utilizando atributo com * [attr*="value"]

# nome = browser.find_element(By.CSS_SELECTOR, "[name*='ome']")
# senha = browser.find_element(By.CSS_SELECTOR, "[name*='nha']")
# btn = browser.find_element(By.CSS_SELECTOR, "[name*='l0']")

# Utilizando atributo com | [attr|="value"]

# nome = browser.find_element(By.CSS_SELECTOR, "[name|='nome']")
# senha = browser.find_element(By.CSS_SELECTOR, "[name|='senha']")
# btn = browser.find_element(By.CSS_SELECTOR, "[name|='l0c0']")

# Utilizando atributo com ^ [attr^="value"]

# nome = browser.find_element(By.CSS_SELECTOR, "[name^='n']")
# senha = browser.find_element(By.CSS_SELECTOR, "[name^='s']")
# btn = browser.find_element(By.CSS_SELECTOR, "[name^='l']")



# browser.close()
