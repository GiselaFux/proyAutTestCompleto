import yaml
import pytest
from src.ui.pages.login_page import LoginPage
from src.ui.pages.inventory_page import InventoryPage

def get_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.mark.ui
@pytest.mark.integration
def test_login_success_integration(driver):
    cfg = get_config()
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page(cfg["base_url"])
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.get_products_count() > 0