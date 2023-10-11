import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
def login_user(driver, open_page):
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()
