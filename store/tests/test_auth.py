import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.django_db
def test_login(live_server, driver, create_user):
    username = "testuser"
    password = "password123"

    create_user(username = username, password = password)

    driver.get(f"{live_server.url}/users/login/")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    WebDriverWait(driver, 5).until(EC.url_changes(f"{live_server.url}/users/login/"))

    driver.get(f"{live_server.url}/users/profile/")
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']") 
    assert username_input.get_attribute("value") == username

@pytest.mark.django_db
def test_logout(live_server, logined_driver):
    logined_driver.get(f"{live_server.url}/")
    logined_driver.find_element(By.XPATH, '//*[@id="navbarDropdown"]/i').click()
    logined_driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[2]/ul/li[4]/a').click()

    login_button = logined_driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li[2]/a')
    assert login_button