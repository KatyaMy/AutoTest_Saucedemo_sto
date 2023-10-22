from pages.main_page import MainPage


class TestSortingList:

    def test_sorting_az(self, driver, correct_user, wait):
        page = MainPage(driver)
        page.sorted_az()

    def test_sorting_za(self, driver, correct_user, wait):
        page = MainPage(driver)
        page.sorted_za()
