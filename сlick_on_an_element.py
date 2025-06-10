from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(2)

# Buscar el botón y hacer clic en él
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

time.sleep(2)

driver.quit()
