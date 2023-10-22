import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import LoginPageLocators

URL = 'https://www.saucedemo.com/'


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait


@pytest.fixture()
def open_page(driver):
    driver.get(URL)


@pytest.fixture(scope="function")
def correct_user(driver, open_page):
    driver.find_element(*LoginPageLocators.username_field).send_keys("standard_user")
    driver.find_element(*LoginPageLocators.password_field).send_keys("secret_sauce")
    driver.find_element(*LoginPageLocators.bt_login).click()
