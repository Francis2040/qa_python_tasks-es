import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("algún_email_registrado")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("alguna_contraseña_registrada")

time.sleep(2)

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "footer")))

# Buscar el pie de página
element = driver.find_element(By.TAG_NAME, "footer")

# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", element)

# Comprobar que el pie de página contiene el string 'Around'
assert 'Around' in element.text
print(" El pie de página contiene el texto 'Around'")

driver.quit()