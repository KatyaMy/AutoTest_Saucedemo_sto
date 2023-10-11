import time
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPage, CartPage



def test_correct_main_page_title(driver, open_page, correct_login):
    expected_title = "Swag Labs"
    app_logo_element = driver.find_element(*MainPage.app_logo_element)
    actual_title = app_logo_element.text
    assert actual_title == expected_title, f"Expected Title '{expected_title}', BUT received '{actual_title}'"


def test_displayed_bt_add_to_cart(driver, open_page, correct_login):
    bt_add_to_cart = driver.find_element(*MainPage.add_to_cart_bt)
    assert bt_add_to_cart.is_enabled()


def test_logout(driver, open_page, correct_login, wait):
    driver.find_element(*MainPage.hamburger_menu).click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bm-item-list")))
    # driver.implicitly_wait(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert driver.current_url == "https://www.saucedemo.com/", "INCORRECT RESULT"


# def test_test(driver, open_page, correct_login):
#     driver.find_element(*MainPage.hamburger_menu).click()
#     # time.sleep(2)
#     driver.find_element(By.ID, "logout_sidebar_link").click()


def test_check_click_shopping_cart(driver, open_page, correct_login):
    driver.find_element(*MainPage.shopping_cart).click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html", "INCORRECT RESULT"

    # shopping_cart_title = driver.find_element(By.CLASS_NAME, "title").text
    # assert shopping_cart_title == "Your Cart"


"""TC check the availability of items in the cart"""


def test_check_item_in_the_cart(driver, open_page, correct_login):
    driver.find_element(*MainPage.add_to_cart_bt).click()
    driver.find_element(*MainPage.shopping_cart).click()
    product_name = driver.find_element(By.ID, "item_4_title_link")
    if product_name:
        print("Item add to cart")
    else:
        print("Item NOT FOUND")


def test_delete_item_from_cart(driver, open_page, correct_login):
    driver.find_element(*MainPage.shopping_cart).click()
    cart_items = driver.find_element(By.ID, "cart_contents_container")
    time.sleep(2)
    item_name = driver.find_element(By.ID, "item_4_title_link")
    remove_item = driver.find_element(*CartPage.remove_button).click()
    # if len(cart_items) > 0:
    #     print("Cart NOT EMPTY")
    # else:
    #     print("Item Removed from cart")
