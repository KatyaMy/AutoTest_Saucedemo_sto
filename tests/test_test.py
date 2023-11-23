import pytest
from selenium.webdriver.common.by import By

print('hello world')
print('Hi')

# results = []
# for product in product_elements:
#     product_name = product.find_element(By.CLASS_NAME, "product-name").text
#     product_price = product.find_element(By.CLASS_NAME, "product-price").text
#     if product_name and product_price:
#         results.append(f"Товар '{product_name}' имеет цену {product_price}")
#     else:
#         results.append(f"Товар '{product_name}' не имеет названия или цены")
#     for result in results:
#         print(result)

@pytest.mark.skip("this test is copy need for check actions")
def test_check_actrions(driver, open_page, correct_user):
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
    driver.find_element(By.XPATH, '//*[@id = "checkout"]').click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html', "Page Not found"


@pytest.mark.skip("this test is copy need for check actions")
def test_check_actrions(driver, open_page, correct_user):
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
    driver.find_element(By.XPATH, '//*[@id = "checkout"]').click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html', "Page Not found"