import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(2)

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("some_email")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("some_password")

time.sleep(2)

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
try:
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "card-section"))
    )
    print("Elemento encontrado y visible.")
except TimeoutException:
    print("El elemento no se pudo encontrar o no es visible.")

# Buscar el botón, recuperar su texto y comprobar que el valor del texto es 'Cerrar sesión'
try:
    element = driver.find_element(By.CLASS_NAME, "card-section")
    if element.text == "Cerrar sesión":
        print("Texto correcto: 'Cerrar sesión'")
    else:
        print(f"Texto inesperado: {element.text}")
except NoSuchElementException:
    print("No se pudo encontrar el elemento 'card-section'.")
except TimeoutException:
    print("El elemento 'card-section' no se pudo encontrar o no es visible.")

driver.quit()

