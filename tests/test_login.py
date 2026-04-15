from pages.login_page import LoginPage

def test_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Verify successful login
    assert "inventory" in driver.current_url
