from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")

    def get_products_count(self) -> int:
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        return len(items)

    def add_first_item_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if buttons:
            buttons[0].click()

    def get_cart_count(self) -> int:
        # Espera hasta que aparezca el badge
        wait = WebDriverWait(self.driver, 10)
        badge = wait.until(EC.presence_of_element_located(self.CART_BADGE))
        return int(badge.text)    