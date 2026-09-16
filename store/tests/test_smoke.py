import pytest


@pytest.mark.django_db
def test_home_page_availability(live_server, driver):
    driver.get(live_server.url)
    
    assert driver.current_url.startswith(live_server.url)