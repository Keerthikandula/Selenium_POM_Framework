import time
from pages.login_page import LoginPage

def test_login(driver, base_url, credentials):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"], credentials["password"])
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    
def test_invalid_password(driver, base_url):
    login = LoginPage(driver)

    login.load(base_url)
    login.login("standard_user", "wrong_password")

    assert "Username and password do not match any user" in login.get_error_message()


def test_invalid_username(driver, base_url):
    login = LoginPage(driver)

    login.load(base_url)
    login.login("wrong_user", "secret_sauce")

    assert "Username and password do not match any user" in login.get_error_message()


def test_empty_username(driver, base_url):
    login = LoginPage(driver)

    login.load(base_url)
    login.login("", "secret_sauce")

    assert "Username is required" in login.get_error_message()


def test_empty_password(driver, base_url):
    login = LoginPage(driver)

    login.load(base_url)
    login.login("standard_user", "")

    assert "Password is required" in login.get_error_message()
    
    