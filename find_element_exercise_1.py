from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Pausa la ejecución durante 5 segundos para permitir que la página se cargue correctamente
time.sleep(5)

title_element = driver.find_element(By.CSS_SELECTOR, ".auth-form__title")

# Buscar e imprimir la linea con el texto
print("Login form title:", title_element.text)

driver.quit()

