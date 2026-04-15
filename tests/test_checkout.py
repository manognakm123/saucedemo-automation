from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")

    inventory.add_to_cart()
    inventory.go_to_cart()

    cart.click_checkout()

    checkout.enter_details()
    checkout.finish_order()

    assert "thank you" in checkout.get_success_message().lower()
