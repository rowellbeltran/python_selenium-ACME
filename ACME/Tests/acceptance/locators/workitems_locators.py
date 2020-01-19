from selenium.webdriver.common.by import By


class WorkitemsPageLocators:
    TABLE_HEADER = By.XPATH, "//*[@class='table']//th"
    TABLE_ROWS = By.XPATH, "//*[@class='table']//tr"
    PAGE_NUMBERS = By.XPATH, "//*[@class='page-numbers' and text()!='>' and text()!='<']"
    CURRENT_PAGE = By.XPATH, "//*[@class ='page-numbers current']"
    SECTION_HEADER = By.XPATH, "//*[@class = 'container-fluid']//h4"

