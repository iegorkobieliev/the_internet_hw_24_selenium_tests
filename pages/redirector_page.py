from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.base_page import BasePage


class RedirectorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    REDIRECT = (By.XPATH, "//a[@href='redirect']")

    @property
    def redirect_link(self) -> webelement:
        return self.find(self.REDIRECT)
