from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Inicializar el navegador
driver = webdriver.Chrome()

# 1. Iniciar sesión
driver.get("https://around-v1.nm.tripleten-services.com/")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "email")))
driver.find_element(By.ID, "email").send_keys("xxxxxxx")
driver.find_element(By.ID, "password").send_keys("xxxxxx")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# 2. Esperar a que aparezca el usuario en la cabecera (login exitoso)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header__user")))

# 3. Guardar el título de la primera tarjeta antes de añadir una nueva
title_before = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text
print("Título antes:", title_before)

# 4. Hacer clic en el botón Agregar
driver.find_element(By.CLASS_NAME, "profile__add-button").click()

# 5. Esperar a que aparezca el popup
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.popup_type_new-card.popup_is-opened")))

# 6. Generar nuevo título aleatorio
random_number = random.randint(100, 999)
new_title = f"Venezuela {random_number}"

# 7. Completar el formulario
driver.find_element(By.NAME, "name").send_keys(new_title)
driver.find_element(By.NAME, "link").send_keys("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")

# 8. Esperar que el botón "Guardar" esté habilitado y hacer clic
guardar_xpath = ".//form[@name='new-card']/button[text()='Save']"
wait.until(lambda d: d.find_element(By.XPATH, guardar_xpath).is_enabled())
driver.find_element(By.XPATH, guardar_xpath).click()

# 9. Esperar que la nueva tarjeta aparezca
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"),new_title))

# 10. Confirmar que la tarjeta se agregó correctamente
title_after = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text
print("Título después:", title_after)
assert title_after == new_title, "El título de la nueva tarjeta no coincide."

# 11. Contar tarjetas antes de eliminar
cards_before_delete = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))

# 12. Hacer clic en el botón Eliminar (primera tarjeta)
delete_button_xpath = "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']"
driver.find_element(By.XPATH, delete_button_xpath).click()

# 13. Esperar a que vuelva a aparecer el título anterior
WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"),title_before))

# 14. Verificar que hay una tarjeta menos
cards_after_delete = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
assert cards_after_delete == cards_before_delete - 1, "La tarjeta no se eliminó correctamente."

print("Test finalizado exitosamente.")

# 15. Esperar unos segundos y cerrar el navegador
time.sleep(2)
driver.quit()