from ui.services.cart_service import CartService
import pytest

@pytest.mark.unit
def test_add_item_increases_count():
    cart = CartService()
    assert cart.total_items() == 0

    cart.add_item("id1", 10.0)
    cart.add_item("id2", 5.5)

    assert cart.total_items() == 2

@pytest.mark.unit
def test_total_price_sums_all_items():
    cart = CartService()
    cart.add_item("id1", 10.0)
    cart.add_item("id2", 5.5)

    assert cart.total_price() == 15.5