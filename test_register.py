import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_register(self):
        driver = self.driver
        driver.get("https://petsocity.vercel.app/registrarUsuario")

        wait = WebDriverWait(driver, 10)

        # Nombre completo
        wait.until(EC.presence_of_element_located((By.ID, "nombreCompleto"))).send_keys("Felipe Tester")

        # Correo y confirmación
        driver.find_element(By.ID, "correo").send_keys("felipe@duoc.cl")
        driver.find_element(By.ID, "verificarCorreo").send_keys("felipe@duoc.cl")

        # Contraseña y confirmación
        driver.find_element(By.ID, "password").send_keys("ClaveSegura1!")
        driver.find_element(By.ID, "verificarPassword").send_keys("ClaveSegura1!")

        # Teléfono
        driver.find_element(By.ID, "telefono").send_keys("912345678")

        # Región y comuna
        Select(driver.find_element(By.ID, "region")).select_by_value("rm")
        Select(driver.find_element(By.ID, "comuna")).select_by_value("linares")

        # Scroll hasta el checkbox de términos y click en el label
        label_terminos = driver.find_element(By.CSS_SELECTOR, "label[for='terminos']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", label_terminos)
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='terminos']")))
            label_terminos.click()
        except:
            driver.execute_script("arguments[0].click();", label_terminos)

        # Scroll hasta el botón Registrar
        btn_registrar = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", btn_registrar)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        btn_registrar.click()

        # Manejar el alert de éxito
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        self.assertIn("Registro exitoso", alert.text)
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
