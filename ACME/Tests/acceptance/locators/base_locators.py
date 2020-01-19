from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.XPATH, "//*[@class='page-header']"
    NAV_BRAND = By.CLASS_NAME, 'navbar-brand'
    NAV_LINKS = By.XPATH, "//div[@id='bs-example-navbar-collapse-1']/ul/li"
    BREADCRUMB = By.XPATH, "//*[@class='breadcrumb']/li"
    CONTAINER_HEADER = By.XPATH, "//*[@class='main-container']/h1"
    PANEL_HEADER = By.CLASS_NAME, 'panel-heading'
    PANEL_TEXT = By.XPATH, "//*[@class='panel-body']/p"
    BUTTONS = By.XPATH, "//*[contains(@class,'btn')]"
    FOOTER = By.TAG_NAME, 'footer'
    FIELD_LABEL = By.TAG_NAME, 'label'

