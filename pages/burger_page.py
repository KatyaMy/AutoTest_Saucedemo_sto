from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import BurgerMenuLocators


class HamburgerMenu(BasePage):
    locator = BurgerMenuLocators

    def check_logout_bt(self, wait):
        self.driver.find_element(*BurgerMenuLocators.burger_menu_bt).click()
        wait.until(EC.visibility_of_element_located(BurgerMenuLocators.item_list))
        self.driver.find_element(*BurgerMenuLocators.bt_logout).click()
        assert self.driver.current_url == "https://www.saucedemo.com/", "BUTTON NOT WORKING"
