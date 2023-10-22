import time
from selenium.webdriver.common.by import By


def test_test(driver, correct_user):
    product_elements = driver.find_element(By.ID, "inventory_container")
    results = []
    for product in product_elements:
        product_name = product.find_element_by_class_name("product-name").text
        product_price = product.find_element_by_class_name("product-price").text
        if product_name and product_price:
            results.append(f"Товар '{product_name}' имеет цену {product_price}")
        else:
            results.append(f"Товар '{product_name}' не имеет названия или цены")
        for result in results:
            print(result)

    # for i in range(3):
    #     product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[i].text
    #     add_to_cart_button = driver.find_elements(By.CLASS_NAME, "btn_inventory")[i]
    #     add_to_cart_button.click()
    #     time.sleep(5)
