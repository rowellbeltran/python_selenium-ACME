from behave import *
from selenium import webdriver

from Tests.acceptance.page.login_page import LoginPage
from Tests.acceptance.page.main_page import MainPage
from Tests.acceptance.page.workitems_page import WorkitemsPage

use_step_matcher('re')

@given('I am on login page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = LoginPage(context.browser)
    context.browser.get(page.url)
    context.browser.maximize_window()

@given('I am on the Main Page')
def step_impl(context):
    context.execute_steps(u'''
    Given I am on login page
    When I enter "valid_value" in "email" field
    And I enter "valid_value" in "password" field
    And I click "Log In" button
    And I wait for the main page to load
    ''')
    page = LoginPage(context.browser)
    context.email = page.credential.get("email")

@given('I am on the Workitems Page')
def step_impl(context):
    context.execute_steps(u'''
    Given I am on the Main Page
    When I click "Work Items" button
    ''')

@then('I am on the main page')
def step_impl(context):
    page = MainPage(context.browser)
    assert context.browser.current_url == page.url

@then('I am on the login page')
def step_impl(context):
    page = LoginPage(context.browser)
    assert context.browser.current_url == page.url

@then('I am on the workitems page')
def step_impl(context):
    page = WorkitemsPage(context.browser)
    assert context.browser.current_url == page.url

@then('From page "(.*)" I am on the "(.*)" page')
def step_impl(context, from_page, to_page):
    page = WorkitemsPage(context.browser)
    if to_page == 'next':
        to_page = int(from_page)+1
    else:
        to_page = len(page.page_numbers)
    assert context.browser.current_url == f'{page.url}/page-{to_page}'


@then('I am on work item details page of WIID: "(.*)"')
def step_impl(context, work_item):
    page = WorkitemsPage(context.browser)
    assert context.browser.current_url == f'{page.url}/{work_item}'






