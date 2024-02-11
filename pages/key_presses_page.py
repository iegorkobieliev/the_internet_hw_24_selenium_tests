from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.base_page import BasePage


class KeyPressesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    INPUT = (By.XPATH, "//input[@id='target']")
    RESULT = (By.XPATH, "//p[@id='result']")
    HEADING3 = (By.XPATH, "//h3")

    @property
    def input(self) -> webelement:
        return self.find(self.INPUT)

    @property
    def result(self) -> webelement:
        return self.find(self.RESULT)

    @property
    def heading3(self) -> webelement:
        return self.find(self.HEADING3)
