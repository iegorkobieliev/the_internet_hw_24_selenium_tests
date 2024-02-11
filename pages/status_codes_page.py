from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.base_page import BasePage


class StatusCodesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def code_200(self) -> webelement:
        return self.find((By.XPATH, "//a[@href='status_codes/200']"))

    @property
    def page_name(self) -> webelement:
        return self.find((By.XPATH, "//h3"))
