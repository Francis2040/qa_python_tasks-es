import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
wait = WebDriverWait(driver, 10)

email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_input.send_keys("anaholef@gmail.com")
password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.send_keys("Fran2040.")

driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header__user")))

# Buscar la tarjeta y desplazarla a la vista
card__image= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".places__list .places__item")))
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });",card__image)

time.sleep(5)

driver.quit()
