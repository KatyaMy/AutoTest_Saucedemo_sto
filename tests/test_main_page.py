from locators.locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    def test_correct_main_page_title(self, driver, correct_user):
        page = MainPage(driver)
        page.correct_main_page_title()

    def test_displayed_bt_add_to_cart(self, driver, correct_user):
        page = MainPage(driver)
        page.displayed_bt_add_to_cart()

    def test_check_click_shopping_cart(self, driver, correct_user):
        page = MainPage(driver)
        page.check_click_shopping_cart()

    def test_sorted_az(self, driver, correct_user):
        page = MainPage(driver)
        page.sorted_az()

    def test_sorted_za(self, driver, correct_user):
        page = MainPage(driver)
        page.sorted_za()
