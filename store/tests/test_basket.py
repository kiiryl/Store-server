import pytest
from selenium.webdriver.common.by import By
from products.models import Product, ProductCategory, Basket

@pytest.mark.django_db
def test_add_product_to_basket(live_server, logined_driver):
    category = ProductCategory.objects.create(name="Одежда")
    Product.objects.create(
        name="Худи", 
        price=1000, 
        quantity=10, 
        category=category
    )

    logined_driver.get(f"{live_server.url}/products/")
    logined_driver.find_element(By.CLASS_NAME, "btn-outline-success").click()
    
    logined_driver.get(f"{live_server.url}/users/profile/")
    assert logined_driver.find_element(By.CSS_SELECTOR, ".badge.badge-secondary.badge-pill").text == '1'


def test_remove_product_from_basket(live_server, logined_driver):
    category = ProductCategory.objects.create(name="Одежда")
    product_to = Product.objects.create(
        name="Худи", 
        price=1000, 
        quantity=10, 
        category=category
    )
    Basket.objects.create(
        user = logined_driver.user, 
        product = product_to, 
        quantity = 1,
    )
    logined_driver.get(f"{live_server.url}/users/profile/")
    logined_driver.find_element(By.CSS_SELECTOR, ".fas.fa-trash").click()
    label = logined_driver.find_element(By.CSS_SELECTOR, ".mt-3.mb-3.d-flex.justify-content-between.align-items-center.mb-3")
    assert label.text == "Корзина пуста"