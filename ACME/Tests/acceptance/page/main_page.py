from Tests.acceptance.page.base_page import BasePage

from Tests.acceptance.locators.main_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return super(MainPage, self).url + '/'

    @property
    def container_note(self):
        return self.driver.find_element(*MainPageLocators.CONTAINER_NOTE)

    @property
    def dropdown_menu(self):
        return self.driver.find_elements(*MainPageLocators.DROPDOWN_MENU)