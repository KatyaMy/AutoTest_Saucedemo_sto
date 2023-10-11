from locators.locators import MainPage, CartPage, BurgerMenu


def test_correct_main_page_title(driver, open_page, correct_login):
    expected_title = "Swag Labs"
    app_logo_element = driver.find_element(*MainPage.app_logo_element)
    actual_title = app_logo_element.text
    assert actual_title == expected_title, f"Expected Title '{expected_title}', BUT received '{actual_title}'"


def test_displayed_bt_add_to_cart(driver, open_page, correct_login):
    bt_add_to_cart = driver.find_element(*MainPage.add_to_cart_bt)
    assert bt_add_to_cart.is_enabled()


# @pytest.skip("This test only test")
# def test_test(driver, open_page, correct_login):
#     driver.find_element(*BurgerMenu.burger_menu_bt).click()
#     time.sleep(2)
#     driver.find_element(*BurgerMenu.bt_logout).click()


def test_check_click_shopping_cart(driver, open_page, correct_login):
    driver.find_element(*MainPage.shopping_cart).click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html", "INCORRECT RESULT"

    # shopping_cart_title = driver.find_element(By.CLASS_NAME, "title").text
    # assert shopping_cart_title == "Your Cart"
