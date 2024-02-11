from pages.home_page import HomePage
from pages.key_presses_page import KeyPressesPage


class App:
    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.key_presses_page = KeyPressesPage(driver)
