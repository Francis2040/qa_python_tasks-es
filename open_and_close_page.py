from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Abrir la página del banco de pruebas
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Comprobar que /signin se agrega a la URL
assert'/signin' in driver.current_url

# Cerrar el navegador
driver.quit()

