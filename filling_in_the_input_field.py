import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(2)

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("some_email")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("some_password")

time.sleep(2)

# Hacer clic en Iniciar sesión
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Esperar a que aparezca un elemento de la página principal tras login
try:
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "header__user"))
    )
    print(" ¡Login exitoso!")

    # Validar la URL
    assert driver.current_url == "https://around-v1.nm.tripleten-services.com/"
    print(" Redirección correcta.")

except TimeoutException:
    print("La informacion es Incorrecta")

driver.quit()