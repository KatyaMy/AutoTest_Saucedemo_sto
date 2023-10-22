from locators.locators import MainPageLocators, CartPageLocators


def test_add_item_in_the_cart(driver, correct_user):
    driver.find_element(*MainPageLocators.add_to_cart_bt).click()
    driver.find_element(*MainPageLocators.shopping_cart).click()
    product_name = driver.find_element(*CartPageLocators.item_4_title)
    if product_name:
        print("Item add to cart")
    else:
        print("Item NOT FOUND")


def test_delete_item_from_cart(driver, correct_user):
    driver.find_element(*MainPageLocators.shopping_cart).click()
    cart_items = driver.find_element(*CartPageLocators.cart_item)
    driver.find_element(*CartPageLocators.item_4_title)
    driver.find_element(*CartPageLocators.remove_button).click()
    if len(cart_items) > 0:
        print("Cart NOT EMPTY")
    else:
        print("Item Removed from cart")


def test_check_item_in_the_cart(driver, correct_user):
    driver.find_element(*MainPageLocators.add_to_cart_bt).click()
    driver.find_element(*MainPageLocators.shopping_cart).click()
    product_name = driver.find_element(*CartPageLocators.item_4_title)
    if product_name:
        print("Item add to cart")
    else:
        print("Item NOT FOUND")
