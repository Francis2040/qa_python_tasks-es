from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# 1. Inicializar navegador y espera
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# 2. Ingresar al sitio y esperar el formulario de login
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
wait.until(EC.presence_of_element_located((By.ID, "email")))

# 3. Iniciar sesión
driver.find_element(By.ID, "email").send_keys("XXXXX")
driver.find_element(By.ID, "password").send_keys("XXXXX")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# 4. Esperar a que el usuario esté logueado
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header__user")))

# 5. Guardar el título de la tarjeta más reciente
title_before = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text
print("Título antes:", title_before)

# 6. Agregar nueva tarjeta
driver.find_element(By.CLASS_NAME, "profile__add-button").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.popup_type_new-card.popup_is-opened")))

# 7. Completar formulario con título aleatorio
random_number = random.randint(100, 999)
new_title = f"Venezuela {random_number}"
driver.find_element(By.NAME, "name").send_keys(new_title)
driver.find_element(By.NAME, "link").send_keys("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")

# 8. Esperar que el botón Guardar esté habilitado y hacer clic
guardar_xpath = ".//form[@name='new-card']/button[text()='Save']"
wait.until(lambda d: d.find_element(By.XPATH, guardar_xpath).is_enabled())
driver.find_element(By.XPATH, guardar_xpath).click()

# 9. Verificar que la nueva tarjeta fue agregada
wait.until(EC.text_to_be_present_in_element(
    (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), new_title
))
print("Nueva tarjeta agregada:", new_title)

# 10. Contar tarjetas antes de eliminar
cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))

# 11. Eliminar la tarjeta (primer botón eliminar visible)
delete_button_xpath = "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']"
driver.find_element(By.XPATH, delete_button_xpath).click()

# 12. Esperar que el título nuevo desaparezca
WebDriverWait(driver, 5).until_not(
    EC.presence_of_element_located((By.XPATH, f"//h2[text()='{new_title}']"))
)

# 13. Confirmar que hay una tarjeta menos
cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
assert cards_after == cards_before - 1, "❌ La tarjeta no se eliminó correctamente."
print("✅ La tarjeta fue eliminada con éxito.")

# 14. Finalizar prueba
time.sleep(2)
driver.quit()