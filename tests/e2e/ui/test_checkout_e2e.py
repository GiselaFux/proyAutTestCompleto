import yaml
import pytest
from src.ui.pages.login_page import LoginPage
from src.ui.pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.e2e
def test_checkout_flow_e2e(driver):
    with open("config/config.yaml") as f:
        cfg = yaml.safe_load(f)

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page(cfg["base_url"])
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == 1

    # Aquí podrías continuar el flujo de checkout, agregando más pasos como ir al carrito, proceder al checkout, etc.