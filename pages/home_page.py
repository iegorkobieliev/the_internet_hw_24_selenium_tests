from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    def __int__(self, driver):
        super().__int__(driver)

    KEY_PRESSES_LINK = (By.XPATH, "//a[@href='/key_presses']")

    def key_presses_link(self):
        return self.find(self.KEY_PRESSES_LINK)
