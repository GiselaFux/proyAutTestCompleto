import os
import yaml
import pytest
from datetime import datetime
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logger.add("logs/suite.log", level="INFO", encoding="utf-8")
    logger.info("=== Test suite started ===")
    yield
    logger.info("=== Test suite finished ===")


@pytest.fixture
def driver(config, request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(config["implicit_wait"])

    yield driver

    # Teardown: si falla, sacar screenshot
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call is not None and getattr(rep_call, "failed", False):
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_name = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        logger.error(f"Screenshot saved to {screenshot_name}")

    driver.quit()


def pytest_runtest_makereport(item, call):
    # Guardamos el reporte de la fase "call" en el item para usarlo en el fixture
    if "driver" in item.fixturenames and call.when == "call":
        item.rep_call = call