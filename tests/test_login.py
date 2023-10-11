import pytest
from locators.locators import LoginPage


@pytest.mark.parametrize("username, password", [("user", "user")])
def test_wrong_login(driver, open_page, username, password):
    username_field = driver.find_element(*LoginPage.username_field)
    username_field.send_keys(username)
    password_field = driver.find_element(*LoginPage.password_field)
    password_field.send_keys(password)
    driver.find_element(*LoginPage.bt_login).click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Incorrect username or password"
