from selenium.common import TimeoutException
from base_page import BasePage
from locators.locators import BurgerMenuLocators

link = "https://www.saucedemo.com/"
labs_link = 'https://saucelabs.com/'


class HamburgerMenu(BasePage):
    locator = BurgerMenuLocators

    def logout_bt(self):
        self.driver.find_element(*BurgerMenuLocators.burger_menu_bt).click()
        self.elements_are_visible(BurgerMenuLocators.item_list)
        self.driver.find_element(*BurgerMenuLocators.bt_logout).click()
        assert self.driver.current_url == link, "Page NOt faund"

    def about_bt(self):
        self.driver.find_element(*BurgerMenuLocators.burger_menu_bt).click()
        self.elements_are_visible(BurgerMenuLocators.item_list)
        self.driver.find_element(*BurgerMenuLocators.bt_about_us).click()
        assert self.driver.current_url == labs_link, "BUTTON NOT WORKING"

    def reset_app_bt(self):
        self.driver.find_element(*BurgerMenuLocators.burger_menu_bt).click()
        self.elements_are_visible(BurgerMenuLocators.item_list)
        try:
            self.element_is_clickable(BurgerMenuLocators.bt_reset_app)
            # если элемент становится кликабельным, продолжает выполнять код
            self.driver.find_element(*BurgerMenuLocators.bt_reset_app).click()
        except TimeoutException:
            print("Button NOT clickable")
