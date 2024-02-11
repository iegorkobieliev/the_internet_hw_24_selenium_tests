from selenium import webdriver

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.key_presses_page import KeyPressesPage


class App:
    def __init__(self, driver: webdriver):
        self.base_page = BasePage(driver)
        self.home_page = HomePage()
        self.key_presses_page = KeyPressesPage()
