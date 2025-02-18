import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')

    service = Service('/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()
