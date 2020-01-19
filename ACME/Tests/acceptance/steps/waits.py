from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Tests.acceptance.page.base_page import BasePageLocators

use_step_matcher('re')


@step('I wait for the main page to load')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(BasePageLocators.TITLE, "Dashboard")
        )
    except:
        raise Exception()

@step('I wait for the URL changes')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(
            expected_conditions.url_changes
        )
    except:
        raise Exception()


@step('I wait for the alert')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(
            expected_conditions.alert_is_present()
        )
    except:
        raise Exception()

