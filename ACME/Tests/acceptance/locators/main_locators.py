from selenium.webdriver.common.by import By


class MainPageLocators:
    CONTAINER_NOTE = By.XPATH, "//*[@class='main-container']/p"
    DROPDOWN_MENU = By.XPATH, "//*[contains(@class, 'dropdown-menu')]/li"

