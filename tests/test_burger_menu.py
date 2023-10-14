from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import BurgerMenuLocators
from pages.burger_page import HamburgerMenu


class TestBurgerPage:

    def test_check_logout_button(self, driver, login_user, wait):
        page = HamburgerMenu(driver)
        page.check_logout_bt(wait)

    def test_check_about_bt(self, driver, login_user, wait):
        driver.find_element(*BurgerMenuLocators.burger_menu_bt).click()
        wait.until(EC.visibility_of_element_located(BurgerMenuLocators.item_list))
        driver.find_element(*BurgerMenuLocators.bt_about_us).click()
        assert driver.current_url == "https://saucelabs.com/", "BUTTON NOT WORKING"

    def test_check_reset_app_bt(self, driver, login_user, wait):
        driver.find_element(*BurgerMenuLocators.burger_menu_bt).click()
        wait.until(EC.visibility_of_element_located(BurgerMenuLocators.item_list))
        try:
            wait.until(EC.element_to_be_clickable(BurgerMenuLocators.bt_reset_app))
            # если элемент становится кликабельным, продолжает выполнять код
            driver.find_element(*BurgerMenuLocators.bt_reset_app).click()
        except TimeoutException:
            print("Button NOT clickable")
