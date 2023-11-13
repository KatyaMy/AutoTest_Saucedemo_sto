import pytest
from selenium import webdriver
from locators.locators import LoginPageLocators


@pytest.mark.parametrize("username, password", [("locked_out_user", "secret_sauce"),
                                                ("problem_user", "secret_sauce"),
                                                ("performance_glitch_user", "secret_sauce")
                                                ])
def test_login(driver, open_page, username, password):
    username_1 = driver.find_element(*LoginPageLocators.username_field)
    password_2 = driver.find_element(*LoginPageLocators.password_field)
    login_button = driver.find_element(*LoginPageLocators.bt_login)

    username_1.send_keys(username)
    password_2.send_keys(password)
    login_button.click()
