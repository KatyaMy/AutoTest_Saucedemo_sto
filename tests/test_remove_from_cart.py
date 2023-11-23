import pytest
from locators.locators import CartPageLocators


def test_remove_from_cart(driver, correct_user):
    # adding item to the cart
    driver.find_element(*CartPageLocators.add_to_cart_button).click()
    # going to the cart:
    driver.find_element(*CartPageLocators.cart_button).click()
    # emptying the cart:
    driver.find_element(*CartPageLocators.cart_bages)
    driver.find_element(*CartPageLocators.cart_item)
    driver.find_element(*CartPageLocators.remove_button).click()
    cart_badge = driver.find_element(*CartPageLocators.cart_container)
    # Проверка что не содержит текст или цифры
    assert not cart_badge.text, "Иконка корзины содержит цифры: {}".format(cart_badge.text)


@pytest.mark.skip()
def test_remove_from_cart2(driver, correct_user, wait):
    # adding item to the cart
    driver.find_element(*CartPageLocators.add_to_cart_button).click()
    # going to the cart:
    driver.find_element(*CartPageLocators.cart_button).click()
    # emptying the cart:
    driver.find_element(*CartPageLocators.cart_bages)
    driver.find_element(*CartPageLocators.cart_item)
    driver.find_element(*CartPageLocators.remove_button).click()
    cart_badge = driver.find_element(*CartPageLocators.cart_container)
    # Check if cart have numbers or text
    assert cart_badge.is_displayed() is False
