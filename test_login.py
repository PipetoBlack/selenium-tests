import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_modal(self):
        driver = self.driver
        wait = self.wait

        # 1) Ir a la página principal
        driver.get("https://petsocity.vercel.app/")

        # 2) Abrir el modal de login: botón outline-primary con PersonCircle
        # Usamos las clases del Button: "btn-outline-primary me-2"
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-primary.me-2"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", login_button)
        login_button.click()

        # 3) Esperar el modal de login
        email_input = wait.until(
            EC.visibility_of_element_located((By.ID, "formBasicEmail"))
        )
        password_input = wait.until(
            EC.visibility_of_element_located((By.ID, "formBasicPassword"))
        )

        # 4) Completar credenciales
        email_input.clear()
        email_input.send_keys("felipe@duoc.cl")
        password_input.clear()
        password_input.send_keys("ClaveSegura1!")

        # 5) Enviar: botón "Iniciar sesión" dentro del modal
        login_submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Iniciar sesión')]"))
        )
        try:
            login_submit.click()
        except Exception:
            # Fallback si no está interactuable (overlay/animación)
            driver.execute_script("arguments[0].click();", login_submit)

        # 6) Validar el mensaje de éxito del Alert dentro del modal
        success_alert = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        assert "Inicio de sesión exitoso" in success_alert.text

        # (Opcional) esperar a que se cierre el modal automáticamente si aplica
        # EC.invisibility_of_element puede fallar si el modal no desaparece; por eso lo envolvemos en try
        try:
            wait.until(EC.invisibility_of_element(success_alert))
        except Exception:
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
