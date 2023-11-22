from pages.burger_page import HamburgerMenu


class TestBurgerPage:

    def test_check_logout_button(self, driver, correct_user):
        page = HamburgerMenu(driver)
        page.logout_bt()

    def test_check_about_but(self, driver, correct_user):
        page = HamburgerMenu(driver)
        page.about_bt()

    def test_check_reset_app_but(self, driver, correct_user, wait):
        page = HamburgerMenu(driver)
        page.reset_app_bt()
