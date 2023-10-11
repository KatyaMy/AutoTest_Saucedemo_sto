from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import BurgerMenu


class HamburgerMenu(BasePage):
    locator = BurgerMenu

    def check_logout_bt(self, wait):
        self.driver.find_element(*BurgerMenu.burger_menu_bt).click()
        wait.until(EC.visibility_of_element_located(BurgerMenu.item_list))
        self.driver.find_element(*BurgerMenu.bt_logout).click()
        assert self.driver.current_url == "https://www.saucedemo.com/", "BUTTON NOT WORKING"
