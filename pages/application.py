from pages.home_page import HomePage
from pages.key_presses_page import KeyPressesPage
from pages.redirector_page import RedirectorPage
from pages.status_codes_page import StatusCodesPage


class App:
    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.key_presses_page = KeyPressesPage(driver)
        self.redirector_page = RedirectorPage(driver)
        self.status_codes_page = StatusCodesPage(driver)
