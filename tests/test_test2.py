
from selenium.webdriver.common.by import By
import time


def test_remove_from_cart(driver, login_user):
    # adding item to the cart
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    # going to the cart:
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()

    # emptying the cart:
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    item = driver.find_element(By.CLASS_NAME, 'cart_item')
    remove_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    time.sleep(2)
    remove_button.click()
    time.sleep(5)
    cart_badge = driver.find_element(By.ID, "shopping_cart_container")
    #
    # Проверка что не содержит текст или цифры
    assert not cart_badge.text, "Иконка корзины содержит цифры: {}".format(cart_badge.text)
    assert cart_badge.is_displayed() is False
    # assert item.is_not_displayed()


