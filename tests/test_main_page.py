from locators.locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    def test_correct_main_page_title(self, driver, correct_user):
        page = MainPage(driver)
        page.correct_main_page_title()

    def test_displayed_bt_add_to_cart(self, driver, correct_user):
        bt_add_to_cart = driver.find_element(*MainPageLocators.add_to_cart_bt)
        assert bt_add_to_cart.is_enabled()

    def test_check_click_shopping_cart(self, driver, correct_user):
        driver.find_element(*MainPageLocators.shopping_cart).click()
        assert driver.current_url == "https://www.saucedemo.com/cart.html", "INCORRECT RESULT"
