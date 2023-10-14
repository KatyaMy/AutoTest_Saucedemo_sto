from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):

    def test_correct_main_page_title(self):
        expected_title = "Swag Labs"
        app_logo_element = self.driver.find_element(*MainPageLocators.app_logo_element)
        actual_title = app_logo_element.text
        assert actual_title == expected_title, f"Expected Title '{expected_title}', BUT received '{actual_title}'"

    def test_displayed_bt_add_to_cart(self):
        bt_add_to_cart = self.driver.find_element(*MainPageLocators.add_to_cart_bt)
        assert bt_add_to_cart.is_enabled()

    def test_check_click_shopping_cart(self):
        self.driver.find_element(*MainPageLocators.shopping_cart).click()
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "INCORRECT RESULT"

        shopping_cart_title = self.driver.find_element(*MainPageLocators.cart_tittle).text
        assert shopping_cart_title == "Your Cart"

    def sorted_az(self):
        unsorted_list = self.driver.find_elements(*MainPageLocators.all_items)
        unsorted_final = []
        for option in unsorted_list:
            unsorted_final.append(option.text)
        unsorted_final.sort()
        self.driver.find_element(*MainPageLocators.SORT_MENU_BUTTON).click()
        self.driver.find_element(*MainPageLocators.sort_az).click()
        self.element_is_present(MainPageLocators.sort_az)
        sorted_list_az = self.driver.find_elements(*MainPageLocators.all_items)
        sorted_az_final = []
        for i in sorted_list_az:
            sorted_az_final.append(i.text)
        assert sorted_az_final == unsorted_final

    def sorted_za(self):
        unsorted_list = self.driver.find_elements(*MainPageLocators.all_items)
        unsorted_final = [option.text for option in unsorted_list]
        sorted_final = sorted(unsorted_final, reverse=True)
        self.driver.find_element(*MainPageLocators.SORT_MENU_BUTTON).click()
        self.driver.find_element(*MainPageLocators.sort_za).click()
        self.element_is_present(MainPageLocators.sort_za)
        sorted_list_za = self.driver.find_elements(*MainPageLocators.all_items)
        sorted_za_final = [i.text for i in sorted_list_za]
        assert sorted_za_final == sorted_final

