from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_field = (By.XPATH, '//input[@data-test="username"]')
    password_field = (By.XPATH, '//input[@data-test="password"]')
    bt_login = (By.XPATH, '//input[@data-test="login-button"]')


class BurgerMenuLocators:
    item_list = (By.CLASS_NAME, "bm-item-list")
    burger_menu_bt = (By.ID, "react-burger-menu-btn")
    bt_logout = (By.ID, "logout_sidebar_link")
    bt_about_us = (By.ID, "about_sidebar_link")
    bt_reset_app = (By.XPATH, "//*[@id='reset_sidebar_link']")


class MainPageLocators:
    add_to_cart_bt = (By.ID, "add-to-cart-sauce-labs-backpack")
    app_logo_element = (By.CLASS_NAME, "app_logo")
    shopping_cart = (By.ID, "shopping_cart_container")
    SORT_MENU_BUTTON = (By.CSS_SELECTOR, ".product_sort_container")
    all_items = (By.CSS_SELECTOR, '.inventory_item_name')
    sort_az = (By.XPATH, "//option[@value='az']")
    sort_za = (By.XPATH, "//option[@value='za']")
    cart_tittle = (By.CLASS_NAME, "title")


class CartPageLocators:
    remove_button = (By.ID, "remove-sauce-labs-backpack")
