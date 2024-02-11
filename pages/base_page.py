from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from settings import BASE_URL


class BasePage:
    def __init__(self, driver: webdriver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def find(self, locator):
        return self._driver.find_element(*locator)

    def wait_for(self, locator):
        return self._wait.until(expected_conditions.presence_of_element_located(locator))

    def open(self, url):
        url = BASE_URL + url
        self._driver.get(url)

    def get_url(self):
        return self._driver.current_url
