import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.application import App
from settings import BASE_URL


@pytest.fixture(scope="module")
def get_driver():
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def get_app(get_driver):
    yield App(get_driver)
