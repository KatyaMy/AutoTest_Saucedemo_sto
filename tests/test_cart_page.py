import time

from selenium.webdriver.common.by import By

from locators.locators import MainPage, CartPage


def test_add_item_in_the_cart(driver, login_user):
    driver.find_element(*MainPage.add_to_cart_bt).click()
    driver.find_element(*MainPage.shopping_cart).click()
    product_name = driver.find_element(By.ID, "item_4_title_link")
    if product_name:
        print("Item add to cart")
    else:
        print("Item NOT FOUND")


def test_delete_item_from_cart(driver, login_user):
    driver.find_element(*MainPage.shopping_cart).click()
    cart_items = driver.find_element(By.ID, "cart_contents_container")
    time.sleep(2)
    driver.find_element(By.ID, "item_4_title_link")
    driver.find_element(*CartPage.remove_button).click()
    if len(cart_items) > 0:
        print("Cart NOT EMPTY")
    else:
        print("Item Removed from cart")
