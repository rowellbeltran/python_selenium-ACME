import pymssql
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from modules.decrypt import decode

from Tests.acceptance.page.base_page import BasePage
from Tests.acceptance.locators.workitems_locators import WorkitemsPageLocators
from Tests.acceptance.test_config import *

class WorkitemsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return super(WorkitemsPage, self).url + '/work-items'

    @property
    def expected_table_headers(self):
        return WORKITEMS_TABLE_HEADER

    def expected_work_item_details(self):
        return WORKITEMS_DETAILS

    @property
    def table_headers(self):
        return self.driver.find_elements(*WorkitemsPageLocators.TABLE_HEADER)

    @property
    def table_data(self):
        return self.driver.find_elements(*WorkitemsPageLocators.TABLE_ROWS)

    @property
    def page_numbers(self):
        return self.driver.find_elements(*WorkitemsPageLocators.PAGE_NUMBERS)

    def icons(self,  button):
        return self.driver.find_elements(By.XPATH, f'//i[contains(@class, \'{button}\')]')

    def page_button(self, name):
        try:
            page_button = self.driver.find_element(By.XPATH, f'//ul[@class=\'page-numbers\']//*[text()=\'{name}\']')
        except NoSuchElementException:
            page_button = None
        return page_button

    @property
    def current_page(self):
        return self.driver.find_element(*WorkitemsPageLocators.CURRENT_PAGE)

    @property
    def table_rows(self):
        return self.driver.find_elements(*WorkitemsPageLocators.TABLE_ROWS)

    def wiid_data(self, work_item, field):
        wiid_index = WORKITEMS_TABLE_HEADER.index("WIID")+1
        try:
            if field == 'all':
                wiid_data = self.driver.find_element(By.XPATH, f'//td[{wiid_index}][text()=\'{work_item}\']/parent::tr/td')
            else:
                field_index = WORKITEMS_TABLE_HEADER.index(field) + 1
                wiid_data = self.driver.find_element(By.XPATH, f'//td[{wiid_index}][text()=\'{work_item}\']/parent::tr/td[{field_index}]')
        except NoSuchElementException:
            wiid_data = None
        return wiid_data

    def work_item_of_row(self, row_num):
        wiid_index = WORKITEMS_TABLE_HEADER.index("WIID") + 1
        row = int(row_num) + 1
        return self.driver.find_element(By.XPATH, f'//*[@class =\'table\']//tr[{row}]/td[{wiid_index}]')

    def row_icon(self, work_item, button):
        wiid_index = WORKITEMS_TABLE_HEADER.index("WIID")+1
        try:
            row_icon = self.driver.find_element(By.XPATH, f'//td[{wiid_index}][text()=\'{work_item}\']/parent::tr//i[contains(@class,\'{button}\')]')

        except NoSuchElementException:
            row_icon = None
        return row_icon

    def work_item_details(self, section):
        return self.driver.find_element(By.XPATH, f'//h4[text()=\'{section}\']/following-sibling::p[1]')

    @property
    def section_header(self):
        return self.driver.find_elements(*WorkitemsPageLocators.SECTION_HEADER)

    def section_details(self, header):
        return self.driver.find_elements(By.XPATH, f'//h4[text()=\'{header}\']/following-sibling::p[1]')

    def ACME_DB_connect(self):
        db_server = ACME_DB_CREDENTIAL.get("server")
        db_name = ACME_DB_CREDENTIAL.get("db")
        db_user = ACME_DB_CREDENTIAL.get("user")
        db_password = decode(ACME_DB_CREDENTIAL.get("password"))
        return pymssql.connect("localhost", "RF_TEST", "RF123", "Test DB")

    def work_item_db(self, work_item):
        db_connection = self.ACME_DB_connect()
        cursor = db_connection.cursor(as_dict=True)
        if work_item == 'all':
            condition = ''
        else:
            condition = f'where WIID = {work_item}'
        cursor.execute(f'SELECT * FROM ACME_work_items {condition}')
        return cursor.fetchall()

