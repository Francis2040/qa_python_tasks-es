from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def avatar_updated(driver, avatar_url):
    try:
        avatar_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "profile__image")))
        style_attr = avatar_element.get_attribute("style")
        print("Style actual:", style_attr)
        return avatar_url in style_attr
    except Exception as e:
        print("Error en avatar_updated:", e)
        return False

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://around-v1.nm.tripleten-services.com/")

driver.implicitly_wait(5)

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("xxxxxxxx")
driver.find_element(By.ID, "password").send_keys("xxxxxx")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Hacer clic en la foto de perfil
avatar_button =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]')))
avatar_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "edit-avatar")))

# Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
input_avatar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//form[@name='edit-avatar']//input[@class='popup__input popup__input_type_description']")))
input_avatar.clear()
input_avatar.send_keys(avatar_url)

time.sleep(1)  # Pequeña espera para que el UI se actualice

save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/form/button[2]')))
save_button.click()

# Verificar que se actualizó la imagen de perfil
WebDriverWait(driver, 15).until(lambda d: avatar_updated(d, avatar_url))
print("Avatar actualizado correctamente")

driver.quit()