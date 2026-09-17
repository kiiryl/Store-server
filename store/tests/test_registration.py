import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from users.models import User

@pytest.mark.django_db
def test_positive_registration(live_server, driver):

    name = 'тест'
    username = 'testuser'
    email = 'test@gmail.com'
    password = 'poiqopp12321!'

    driver.get(f"{live_server.url}/users/register/")
    driver.find_element(By.ID, 'id_first_name').send_keys(name)
    driver.find_element(By.ID, 'id_last_name').send_keys(name)
    driver.find_element(By.ID, 'id_username').send_keys(username)
    driver.find_element(By.ID, 'id_email').send_keys(email)
    driver.find_element(By.ID, 'id_password1').send_keys(password)
    driver.find_element(By.ID, 'id_password2').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block').click()

    WebDriverWait(driver, 5).until(EC.url_changes(f"{live_server.url}/users/register/"))

    db_user = User.objects.get(username=username)
    assert db_user.username == username
