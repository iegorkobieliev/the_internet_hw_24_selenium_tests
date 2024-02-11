from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.base_page import BasePage


class StatusCodesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def page_name(self) -> webelement:
        return self.find((By.XPATH, "//h3"))

    @property
    def code_200(self) -> webelement:
        return self.find((By.XPATH, "//a[@href='status_codes/200']"))

    def code_number(self, code) -> webelement:
        return self.find((By.XPATH, f"//a[@href='status_codes/{code}']"))

    @property
    def content(self) -> webelement:
        return self.find((By.XPATH, "//p"))
