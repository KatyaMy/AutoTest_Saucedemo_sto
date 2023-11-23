import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import LoginPageLocators
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

URL = 'https://www.saucedemo.com/'


@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        driver.set_window_size(1382, 754)
    else:
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=Service())
        driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait


@pytest.fixture()
def open_page(driver):
    driver.get(URL)


@pytest.fixture(scope="function")
def correct_user(driver, open_page):
    driver.find_element(*LoginPageLocators.username_field).send_keys("standard_user")
    driver.find_element(*LoginPageLocators.password_field).send_keys("secret_sauce")
    driver.find_element(*LoginPageLocators.bt_login).click()
