# Proyecto Final – Framework de Automatización (UI + API + BDD + CI/CD)

Framework de automatización de pruebas en Python que cubre:
- Pruebas de UI con Selenium WebDriver sobre [SauceDemo](https://www.saucedemo.com/).
- Pruebas de API sobre [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
- Escenarios BDD con Behave.
- Ejecución automatizada en CI/CD con GitHub Actions.

Este proyecto está pensado como un framework modular y extensible, siguiendo buenas prácticas de Page Object Model, separación de capas (unit, integration, e2e) y reportes detallados. [web:22][web:23][web:39][web:42][web:46][web:58][web:60]

---

## Tecnologías utilizadas

- **Lenguaje**: Python 3.x
- **Framework de testing**: Pytest
- **UI Testing**: Selenium WebDriver + Page Object Model
- **API Testing**: Requests
- **BDD**: Behave (Gherkin)
- **Reportes**: pytest-html
- **Logging**: loguru
- **Gestión de drivers**: webdriver-manager
- **Control de versiones**: Git + GitHub
- **CI/CD**: GitHub Actions

[web:22][web:23][web:39][web:42][web:43][web:55][web:58][web:60][web:61][web:62]

---

## Estructura del proyecto

```bash
proyecto-final-automation-testing-nombre-apellido/
├── .github/
│   └── workflows/
│       └── ci.yml                # Pipeline CI (unit, integration, e2e + BDD)
├── behave/
│   ├── features/
│   │   ├── login.feature         # Escenarios BDD para login en SauceDemo
│   │   └── environment.py        # Hooks de Behave (before_all, before_scenario, etc.)
│   └── steps/
│       └── login_steps.py        # Implementación de steps BDD
├── config/
│   └── config.yaml               # Configuración (URLs, browser, waits)
├── data/
│   ├── ui_test_data.csv          # Datos de prueba UI (ej: login parametrizado)
│   └── api_test_data.json        # Datos de prueba API (payloads de JSONPlaceholder)
├── logs/
│   └── suite.log                 # Log de ejecución (generado en runtime)
├── pages/
│   ├── base_page.py              # BasePage con acciones genéricas
│   ├── login_page.py             # Page Object de la pantalla de login
│   ├── inventory_page.py         # Page Object de listado de productos
│   └── __init__.py
├── reports/
│   └── pytest_report.html        # Reportes HTML de Pytest (generados en runtime)
├── screenshots/
│   └── *.png                     # Screenshots de fallos (generados en runtime)
├── src/
│   ├── api/
│   │   ├── client.py             # Cliente genérico para requests HTTP
│   │   └── services.py           # Lógica de negocio sobre JSONPlaceholder
│   └── ui/
│       └── services/
│           └── cart_service.py   # Lógica de carrito en memoria (unit tests)
├── tests/
│   ├── unit/
│   │   ├── ui/
│   │   │   └── test_cart_service_unit.py
│   │   └── api/
│   │       └── test_services_unit.py
│   ├── integration/
│   │   ├── ui/
│   │   │   └── test_login_flow_integration.py
│   │   └── api/
│   │       └── test_posts_integration.py
│   └── e2e/
│       └── ui/
│           └── test_checkout_e2e.py
├── tests/conftest.py             # Fixtures: driver, config, logging, screenshots
├── .gitignore
├── pytest.ini                    # Configuración de Pytest (markers, reportes)
├── requirements.txt              # Dependencias del proyecto
├── run_all_tests.py              # Script para ejecutar Pytest + Behave
└── README.md
```

La estructura separa claramente:
- Código de UI, API y servicios.
- Niveles de prueba: unit, integration, e2e.
- BDD en una carpeta propia (`behave/`).
- Recursos comunes: datos, configuración, logs, reportes y screenshots. [web:22][web:23][web:34][web:37][web:39][web:42][web:46][web:58][web:60][web:61]

---

## Instalación y configuración del entorno

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/proyecto-final-automation-testing-nombre-apellido.git
cd proyecto-final-automation-testing-nombre-apellido
```

[web:47][web:48][web:51]

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
```

- Activar en Windows (CMD):

```bash
venv\Scripts\activate
```

- Activar en Linux/macOS:

```bash
source venv/bin/activate
```

[web:48][web:49][web:51][web:54]

### 3. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Esto instala Pytest, Selenium, Requests, Behave, webdriver-manager, PyYAML, loguru y plugins necesarios. [web:48][web:49][web:51][web:54][web:55]

---

## Cómo ejecutar las pruebas

### 1. Ejecutar todos los tests Pytest (unit + integration + e2e)

Desde la raíz del proyecto, con el entorno virtual activado:

```bash
pytest -v
```

Generará un reporte HTML en `reports/pytest_report.html`. [web:23][web:56][web:58][web:62]

### 2. Ejecutar solo unit tests

```bash
pytest tests/unit -m unit -v
```

Estos tests no usan Selenium ni HTTP real; prueban lógica pura (por ejemplo, `cart_service` y `PostsService` con clientes falsos). [web:33][web:34][web:37]

### 3. Ejecutar solo integration tests

```bash
pytest tests/integration -m integration -v
```

- **UI integration**: se conecta con SauceDemo usando Selenium + Page Objects.
- **API integration**: se conecta con JSONPlaceholder usando requests reales. [web:31][web:33][web:36][web:42]

### 4. Ejecutar solo E2E UI

```bash
pytest tests/e2e/ui -m "ui and e2e" -v
```

Simula un flujo de usuario completo (login + agregar producto al carrito, etc.). [web:31][web:32][web:33][web:39]

### 5. Ejecutar BDD con Behave

```bash
behave behave/features
```

Esto ejecuta los escenarios definidos en `login.feature`, reutilizando los mismos Page Objects y driver que Pytest. [web:43][web:46][web:61]

### 6. Ejecutar todo (Pytest + Behave) con un solo comando

```bash
python run_all_tests.py
```

Este script corre primero la suite Pytest (UI + API, todos los niveles) y luego los escenarios BDD, generando reportes y logs correspondientes. [web:10][web:18][web:24]

---

## Reportes y artefactos

- **Reportes HTML de Pytest**:  
  Se generan en la carpeta `reports/` (por defecto `reports/pytest_report.html`, o reportes separados por job en CI). [web:23][web:56][web:58][web:62]  

- **Resultados Behave**:  
  El comando de Behave guarda un `reports/behave.json` que puede consumirse luego por otras herramientas o para análisis. [web:43][web:46]  

- **Logs**:  
  Toda la ejecución se registra en `logs/suite.log` mediante loguru, incluyendo inicio y fin de la suite y errores relevantes. [web:19][web:23][web:60]  

- **Screenshots**:  
  Cuando un test de UI falla, se captura automáticamente un screenshot en `screenshots/`, con nombre que incluye el nombre del test y la fecha/hora. [web:19][web:23][web:39][web:44]

---

## Estrategia de testing (piramide de pruebas)

Este framework sigue la **Testing Pyramid**:

- **Unit tests** (`tests/unit`):
  - Prueban lógica pequeña y aislada (servicios UI sin Selenium, servicios API con clientes falsos).
  - Son muy rápidos y numerosos. [web:31][web:33][web:34][web:36]

- **Integration tests** (`tests/integration`):
  - Verifican la interacción entre componentes: Page Objects + Selenium + SauceDemo, o servicios API + JSONPlaceholder real. [web:31][web:33][web:36][web:37]

- **E2E tests** (`tests/e2e`):
  - Pocos, pero cubren flujos completos de negocio de extremo a extremo en UI. [web:31][web:32][web:33][web:36]

- **BDD (Behave)**:
  - Escenarios de negocio legibles por negocio/QA que se mapean a Page Objects y servicios existentes. [web:32][web:33][web:43][web:46][web:61]

---

## Integración Continua (CI/CD) con GitHub Actions

El pipeline de CI se define en `.github/workflows/ci.yml` y se ejecuta automáticamente en:

- `push` a las ramas `main` y `develop`.
- `pull_request` hacia `main` y `develop`. [web:3][web:18][web:24][web:58][web:59][web:62]

### Jobs principales

1. **unit-tests**  
   - Instala dependencias.  
   - Ejecuta `pytest tests/unit -m unit`.  
   - Genera reporte `reports/unit_report.html`.  
   - Sube el reporte como artefacto. [web:3][web:18][web:24][web:58]

2. **integration-tests** (depende de unit-tests)  
   - Ejecuta `pytest tests/integration -m integration`.  
   - Genera `reports/integration_report.html`.  
   - Sube el reporte como artefacto. [web:3][web:18][web:24][web:58]

3. **e2e-and-bdd** (depende de integration-tests)  
   - Ejecuta E2E UI (`pytest tests/e2e/ui -m "ui and e2e"`).  
   - Ejecuta BDD (`behave behave/features`).  
   - Sube reportes y resultados de Behave como artefactos. [web:3][web:18][web:24][web:58][web:62]

Esto asegura que:
- El código no se integra si fallan los unit tests.
- Las integraciones y E2E/BDD solo corren si la base está estable.
- Los resultados quedan visibles en la pestaña **Actions** de GitHub, con reportes descargables. [web:3][web:18][web:24][web:58][web:59][web:62]

---

## Control de versiones y flujo de trabajo sugerido

- Trabajar en ramas feature (`feature/ui-login-tests`, `feature/api-posts-tests`, etc.).
- Abrir Pull Requests hacia `develop` o `main`.
- Dejar que GitHub Actions ejecute la CI; solo mergear cuando todos los checks estén en verde. [web:24][web:58][web:59][web:60]
- Mantener mensajes de commit descriptivos (por ejemplo: `Add API integration tests for posts`).

---

## Cómo extender el framework

Algunas ideas para crecer el proyecto:

- Agregar más Page Objects (detalle de producto, carrito, checkout completo).
- Incluir más endpoints de JSONPlaceholder (comments, users, etc.).
- Añadir más features BDD (por ejemplo, flujos de compra). [web:39][web:42][web:46][web:61]
- Integrar Allure u otra herramienta de reportes avanzados.
- Ejecutar tests en diferentes navegadores/OS usando matrices de GitHub Actions. [web:35][web:38][web:58]

---

## Autor

- **Nombre:** TU NOMBRE  
- **Rol:** QA Automation / Python Test Engineer  
- **Repositorio:** `https://github.com/TU_USUARIO/proyecto-final-automation-testing-nombre-apellido`