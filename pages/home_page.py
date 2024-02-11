from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    KEY_PRESSES_LINK = (By.XPATH, "//a[@href='/key_presses']")

    @property
    def key_presses_link(self):
        return self.find(self.KEY_PRESSES_LINK)
