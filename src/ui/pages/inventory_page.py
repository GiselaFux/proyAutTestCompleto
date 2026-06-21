from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")

    def get_products_count(self) -> int:
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        return len(items)

    def add_first_item_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if buttons:
            buttons[0].click()

    def get_cart_count(self) -> int:
        badge = self.driver.find_element(*self.CART_BADGE)
        return int(badge.text)