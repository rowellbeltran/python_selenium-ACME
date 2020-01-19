from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Tests.acceptance.page.login_page import LoginPage
from Tests.acceptance.page.main_page import MainPage
from Tests.acceptance.page.workitems_page import WorkitemsPage

use_step_matcher('re')

@step('I enter "(.*)" in "(.*)" field')
def step_impl(context, content, field_name):
    page = LoginPage(context.browser)
    field_element = page.input_field(field_name)
    if content == 'valid_value' and (field_name in ['email', 'password']):
        value = page.credential.get(field_name)
        field_element.send_keys(value)
    else:
        field_element.send_keys(content)

@step('I click "(.*)" button')
def step_impl(context, content):
    page = LoginPage(context.browser)
    buttons = page.buttons
    field = [button for button in buttons if button.text == content]
    field[0].click()

@step('I click "(.*)" link from navigation bar')
def step_impl(context, content):
    page = MainPage(context.browser)
    element = page.nav_links
    links = [l for l in element if l.text == content]
    links[0].click()

@step('I click on "(.*)" page button')
def step_impl(context, content):
    page = WorkitemsPage(context.browser)
    if content == 'last':
        page_num = len(page.page_numbers)
    else:
        page_num = content
    button = page.page_button(page_num)
    button.click()

@step('I click on "(.*)" from breadcrumbs')
def step_impl(context, content):
    page = WorkitemsPage(context.browser)
    breadcrumbs = page.breadcrumbs
    links = [l for l in breadcrumbs if l.text == content]
    links[0].click()

@step('I click on "(.*)" from navigation bar')
def step_impl(context, content):
    page = WorkitemsPage(context.browser)
    nav_links = page.nav_links
    links = [l for l in nav_links if l.text == content]
    links[0].click()

@step('I click on "(.*)" button of WIID: "(.*)"')
def step_impl(context, icon, work_item):
    page = WorkitemsPage(context.browser)
    button = page.row_icon(work_item, icon)
    while button is None:
        page.page_button('>').click()
        button = page.row_icon(work_item, icon)
    button.click()



