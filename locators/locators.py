from selenium.webdriver.common.by import By


class LoginPage:
    username_field = (By.XPATH, '//input[@data-test="username"]')
    password_field = (By.XPATH, '//input[@data-test="password"]')
    bt_login = (By.XPATH, '//input[@data-test="login-button"]')


class BurgerMenu:
    item_list = (By.CLASS_NAME, "bm-item-list")
    burger_menu_bt = (By.ID, "react-burger-menu-btn")
    bt_logout = (By.ID, "logout_sidebar_link")
    bt_about_us = (By.ID, "about_sidebar_link")
    bt_reset_app = (By.XPATH, "//*[@id='reset_sidebar_link']")


class MainPage:
    add_to_cart_bt = (By.ID, "add-to-cart-sauce-labs-backpack")
    app_logo_element = (By.CLASS_NAME, "app_logo")
    shopping_cart = (By.ID, "shopping_cart_container")


class CartPage:
    remove_button = (By.ID, "remove-sauce-labs-backpack")
