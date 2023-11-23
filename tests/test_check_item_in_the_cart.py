import time

from selenium.webdriver.common.by import By


def test_check_add_3_item_in_the_cart(driver, correct_user, wait):
    driver.find_elements(By.CLASS_NAME, "inventory_container")
    for i in range(3):
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        add_to_cart_buttons[i].click()
    driver.find_element(By.ID, 'shopping_cart_container').click()
    time.sleep(3)
    assert driver.current_url == 'https://www.saucedemo.com/cart.html', 'Page NOT FOUND'
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 3, f"Ожидалось 3 товара в корзине, но обнаружено {len(cart_items)}"
