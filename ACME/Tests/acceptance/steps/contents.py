from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Tests.acceptance.page.base_page import BasePage
from Tests.acceptance.page.login_page import LoginPage
from Tests.acceptance.page.main_page import MainPage
from Tests.acceptance.page.workitems_page import WorkitemsPage
from Tests.acceptance.locators.workitems_locators import WorkitemsPageLocators

use_step_matcher('re')

#Base Page
@step('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    tag = page.title
    assert tag is not None
    assert tag.is_displayed()


@step('The title tag contains "(.*)"')
def step_impl(context, content):
    page = BasePage(context.browser)
    tag = page.title
    assert tag.text == content

@step('The navigation bar header "(.*)" is displayed')
def step_impl(context, content):
    page = BasePage(context.browser)
    header = page.nav_bar_header
    assert header.text == content

@step('The navigation link "(.*)" is displayed')
def step_impl(context, content):
    page = BasePage(context.browser)
    element = page.nav_links
    nav_links = [link for link in element if link.text == content]
    assert len(nav_links) > 0
    assert nav_links[0].is_displayed()

@step('The breadcrumb "(.*)" is displayed')
def step_impl(context, content):
    page = BasePage(context.browser)
    element = page.breadcrumbs
    breadcrumbs = [bc for bc in element if bc.text == content]
    assert len(breadcrumbs) > 0
    assert breadcrumbs[0].is_enabled()

@step('There is a field label "(.*)" displayed')
def step_impl(context, content):
    page = BasePage(context.browser)
    element = page.field_labels
    labels = [label for label in element if label.text == content]
    assert len(labels) > 0
    assert labels[0].is_displayed()

@step('There is a text field "(.*)" displayed')
def step_impl(context, content):
    page = BasePage(context.browser)
    element = page.input_field(content)
    assert element.is_displayed()
    assert element.is_enabled()

@step('There is a "(.*)" button displayed')
def step_impl(context, content):
    page = BasePage(context.browser)
    element = page.buttons
    buttons = [b for b in element if b.text == content]
    assert len(buttons) > 0
    assert buttons[0].is_displayed
    assert buttons[0].is_enabled()

@then('Alert message "(.*)" is displayed')
def step_impl(context, content):
    alert = context.browser.switch_to.alert
    assert alert.text == content

#Log In Page
@step('Login Page displays container header')
def step_impl(context):
    page = LoginPage(context.browser)
    header = page.container_header
    assert header is not None

@step('Login Page container header tag contains "(.*)"')
def step_impl(context, content):
    page = LoginPage(context.browser)
    header = page.container_header
    assert header.text == content, f'Expected: {content}, Actual: {header.text}'

@step('There is a footer shown on the page')
def step_impl(context):
    page = LoginPage(context.browser)
    footer = page.footer
    assert footer is not None

@step('The text displayed is "(.*)"')
def step_impl(context, content):
    page = LoginPage(context.browser)
    footer = page.footer
    assert footer.text == content


#Main Page
@step('Main Page displays container header')
def step_impl(context):
    page = MainPage(context.browser)
    header = page.container_header
    assert header is not None

@step('Main Page container header tag contains "(.*)" "(.*)""(.*)"')
def step_impl(context, content1, email, content2):
    page = MainPage(context.browser)
    header = page.container_header
    assert header.text == content1 + context.email + content2

@step('Container note displays "(.*)"')
def step_impl(context, content):
    page = MainPage(context.browser)
    note = page.container_note
    assert note.text == content

@step('"(.*)" is available from the dropdown menu')
def step_impl(context, content):
    page = MainPage(context.browser)
    element = page.dropdown_menu
    menu = [m for m in element if m.text == content]
    assert len(menu) > 0
    assert menu[0].is_displayed()
    assert menu[0].is_enabled()

@step('The panel header displays "(.*)"')
def step_impl(context, content):
    page = BasePage(context.browser)
    panel_header = page.panel_header
    assert panel_header.is_displayed()
    assert panel_header.text == content

@step('The panel text displays "(.*)"')
def step_impl(context, content):
    page = BasePage(context.browser)
    panel_text = page.panel_text
    assert panel_text.is_displayed()
    assert panel_text.text == content

#Work Items Page
@step('The table displays row headers')
def step_impl(context):
    page = WorkitemsPage(context.browser)
    expected_headers = page.expected_table_headers
    actual_headers = page.table_headers

    headers = [h for h in actual_headers if h.text in expected_headers]

    assert len(expected_headers) == len(headers)

@step('The table displays max of 10 rows')
def step_impl(context):
    page = WorkitemsPage(context.browser)
    row_count = len(page.table_data)-1
    page_count = len(page.page_numbers)
    if page_count > 1:
        assert row_count == 10, f'actual: {row_count}, expected: {10}'
    elif page_count == 1:
        assert row_count < 10, f'actual: {row_count}, expected: {10}'

@step('Each row contains "(.*)" icon')
def step_impl(context, content):
    page = WorkitemsPage(context.browser)
    icons = page.icons(content)
    row_count = len(page.table_data)-1
    assert len(icons) == row_count

@step('The page numbers are displayed')
def step_impl(context):
    page = WorkitemsPage(context.browser)
    page_numbers = page.page_numbers
    assert len(page_numbers) > 0

@step('"(.*)" page number is "(.*)" and "(.*)"')
def step_impl(context, page_num, display, enable):
    page = WorkitemsPage(context.browser)
    page_button = page.page_button(page_num)

    #Displayed?
    if display == 'not displayed':
        assert page_button is None
    else:
        assert page_button.is_displayed()
        href = page_button.get_attribute('href')
        #Enabled?
        if enable == 'not enabled':
            assert href is None
        else:
            assert href is not None

@step('Count of work items is the same as database')
def step_impl(context):
    page = WorkitemsPage(context.browser)
    db_data = page.work_item_db('all')
    all_rows_count = len(page.table_rows)-1
    while page.page_button('>') is not None:
        page.page_button('>').click()
        all_rows_count += len(page.table_rows)-1
    assert all_rows_count == len(db_data), f'actual: {all_rows_count}, expected: {len(db_data)}'

@step('The correct "(.*)" is displayed for WIID: "(.*)"')
def step_impl(context, field, item):
    page = WorkitemsPage(context.browser)

    #DB
    query = page.work_item_db(item)
    db_value = query[0].get(field)

    #UI
    display = page.wiid_data(item, field)
    while display is None:
        page.page_button('>').click()
        display = page.wiid_data(item, field)

    assert db_value == display.text, f'actual: {db_value}, expected: {display.text}'


@step('The "(.*)" section header is displayed')
def step_impl(context, content):
    page = WorkitemsPage(context.browser)
    element = page.section_header
    headers = [h for h in element if h.text == content]
    assert len(headers) > 0
    assert headers[0].is_displayed()

@step('The correct "(.*)" is displayed for WIID: "(.*)" in Work Item Details Section')
def step_impl(context, field, work_item):
    page = WorkitemsPage(context.browser)
    #UI
    details = page.section_details('Work Item Details')
    split_value = details[0].text.splitlines()
    ui_value = [f for f in split_value if f.startswith(field)]

    #DB
    query = page.work_item_db(work_item)
    if field == 'Type':
        db_value = query[0].get('Description')
    else:
        db_value = query[0].get(field)
    expected = f'{field}: {db_value}'

    assert details[0].is_displayed()
    assert ui_value[0] == expected, f'Expected: {expected}, Actual: {ui_value[0]}'















