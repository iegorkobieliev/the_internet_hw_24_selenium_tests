from selenium import webdriver
from selenium.webdriver.remote import webelement

from pages.base_page import BasePage


class KeyPressesPage(BasePage):
    def __int__(self, driver):
        super().__int__(driver)
        self.input: webelement = self.find("//input[@id='target']")


