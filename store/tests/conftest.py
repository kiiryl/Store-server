import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    web_driver = webdriver.Chrome(options=options)
    web_driver.implicitly_wait(5)

    yield web_driver
    web_driver.quit()


@pytest.fixture
def create_user(db):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    def _make_user(username="testuser", password="password123", **extra_fields):
        user = User.objects.create_user(
            username=username, password=password, **extra_fields
        )
        user.raw_password = password
        return user
    
    return _make_user

@pytest.fixture
def logined_driver(driver, live_server, create_user):    
    username = "testuser"
    password = "password123"

    user = create_user(username = username, password = password)
    
    driver.get(f"{live_server.url}/users/login/")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    WebDriverWait(driver, 5).until(EC.url_changes(f"{live_server.url}/users/login/"))
    driver.user = user
    yield driver