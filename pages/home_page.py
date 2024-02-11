from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    KEY_PRESSES_LINK = (By.XPATH, "//a[@href='/key_presses']")
    REDIRECT_LINK = (By.XPATH, "//a[@href='/redirector']")

    @property
    def key_presses_link(self):
        return self.find(self.KEY_PRESSES_LINK)

    @property
    def redirect_link(self):
        return self.find(self.REDIRECT_LINK)

    @property
    def status_codes_link(self):
        return self.find((By.XPATH, "//a[@href='/status_codes']"))

