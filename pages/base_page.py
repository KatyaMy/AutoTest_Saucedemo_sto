from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class BasePage:

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def check_element_visibility(self, locator, wait):
        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    # def open_page(self):
    #     self.driver.get(self.link)

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
