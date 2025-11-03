# 🐾 Tutorial Completo de Automatización de Pruebas con Selenium en PetSocity

Este documento guía paso a paso la configuración de entorno, instalación
de dependencias y ejecución de pruebas automatizadas con **Selenium** en
el proyecto **PetSocity**, validando flujos críticos como login y
registro.

------------------------------------------------------------------------

## ✅ Requisitos Previos

Asegúrate de contar con los siguientes componentes instalados:

-   **Python 3.10+**
-   **pip**
-   **Google Chrome** actualizado
-   **Git** (opcional)

------------------------------------------------------------------------

## ⚙️ Configuración del Entorno

### 1️⃣ Crear entorno virtual

``` bash
python -m venv venv
```

### 2️⃣ Activar entorno virtual

**Windows**

``` bash
venv\Scripts\activate
```

**Mac/Linux**

``` bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

``` bash
pip install selenium webdriver-manager
```

**Descripción de librerías** - `selenium`: librería principal para
automatizar navegadores - `webdriver-manager`: gestiona automáticamente
el driver de Chrome

------------------------------------------------------------------------

## 📂 Estructura del Proyecto

    selenium-tests/
    │
    ├── test_login.py        # Prueba automatizada de login
    ├── test_register.py     # Prueba automatizada de registro
    └── README.md            # Documentación general

------------------------------------------------------------------------

## 🚀 Ejecución de Pruebas

Ejecutar un test específico:

``` bash
python -m unittest test_login.py
```

Ejecutar todos los tests del directorio:

``` bash
python -m unittest discover
```

------------------------------------------------------------------------

## 📝 Ejemplo Completo: Prueba de Login

``` python
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

        driver.get("https://petsocity.vercel.app/")

        # Abrir modal de login
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-primary.me-2"))
        )
        login_button.click()

        # Completar credenciales
        driver.find_element(By.ID, "formBasicEmail").send_keys("felipe@duoc.cl")
        driver.find_element(By.ID, "formBasicPassword").send_keys("ClaveSegura1!")

        # Click en iniciar sesión
        login_submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Iniciar sesión')]"))
        )
        login_submit.click()

        # Validación de mensaje
        success_alert = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        self.assertIn("Inicio de sesión exitoso", success_alert.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

------------------------------------------------------------------------

## 🔎 Conceptos Importantes

  -----------------------------------------------------------------------
  Concepto                                      Uso
  --------------------------------------------- -------------------------
  Selenium WebDriver                            Control del navegador

  WebDriverWait + ExpectedConditions            Esperas explícitas para
                                                elementos dinámicos

  `unittest`                                    Framework de pruebas en
                                                Python

  `scrollIntoView()` + JS click                 Manejo de elementos
                                                ocultos

  webdriver-manager                             Driver de Chrome
                                                automático
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🐞 Troubleshooting

  -----------------------------------------------------------------------
  Problema                            Solución
  ----------------------------------- -----------------------------------
  TimeoutException                    Revisar selectores, usar
                                      `wait.until()`

  Elemento no interactuable           Aplicar scroll o ejecutar
                                      JavaScript click

  Driver no encontrado                Usar `webdriver-manager`
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## ✅ Conclusión

Con esta configuración podrás automatizar pruebas criticas como login y
registro, replicando interacciones reales del usuario y asegurando el
correcto funcionamiento de la plataforma **PetSocity**.

> 🚀 Automatización = Menos errores + Más calidad + Mejor desarrollo
> continuo

------------------------------------------------------------------------

© 2025 --- Documentación de QA Automation para PetSocity
