import pytest
from selenium.webdriver.common.by import By
from products.models import Product, ProductCategory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.django_db
def test_add_product_to_basket(live_server, driver, create_user):
    category = ProductCategory.objects.create(name="Одежда")
    Product.objects.create(
        name="Худи", 
        price=1000, 
        quantity=10, 
        category=category
    )
    user = create_user(username="buyer", password="password123")

    driver.get(f"{live_server.url}/users/login/")
    driver.find_element(By.NAME, "username").send_keys("buyer")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    WebDriverWait(driver, 5).until(EC.url_changes(f"{live_server.url}/users/login/"))
    
    driver.get(f"{live_server.url}/products/")
    driver.find_element(By.CLASS_NAME, "btn-outline-success").click()
    
    driver.get(f"{live_server.url}/users/profile/")
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']") 
    assert username_input.get_attribute("value") == "buyer"
    assert driver.find_element(By.CSS_SELECTOR, ".badge.badge-secondary.badge-pill").text == '1'