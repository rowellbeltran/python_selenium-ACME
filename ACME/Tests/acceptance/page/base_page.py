from selenium.webdriver.common.by import By

from Tests.acceptance.locators.base_locators import BasePageLocators
from Tests.acceptance.test_config import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return ACME_URL

    @property
    def nav_bar_header(self):
        return self.driver.find_element(*BasePageLocators.NAV_BRAND)

    @property
    def nav_links(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def footer(self):
        return self.driver.find_element(*BasePageLocators.FOOTER)

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def breadcrumbs(self):
        return self.driver.find_elements(*BasePageLocators.BREADCRUMB)

    @property
    def container_header(self):
        return self.driver.find_element(*BasePageLocators.CONTAINER_HEADER)

    @property
    def field_labels(self):
        return self.driver.find_elements(*BasePageLocators.FIELD_LABEL)

    def input_field(self, field_name):
        return self.driver.find_element(By.NAME, field_name)

    @property
    def buttons(self):
        return self.driver.find_elements(*BasePageLocators.BUTTONS)

    @property
    def panel_header(self):
        return self.driver.find_element(*BasePageLocators.PANEL_HEADER)

    @property
    def panel_text(self):
        return self.driver.find_element(*BasePageLocators.PANEL_TEXT)


