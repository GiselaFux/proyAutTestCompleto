from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout: int = 10):
        self.find(locator, timeout).click()

    def type(self, locator, text: str, timeout: int = 10):
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout: int = 10) -> str:
        return self.find(locator, timeout).text