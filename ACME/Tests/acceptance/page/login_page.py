
from modules.decrypt import decode

from Tests.acceptance.page.base_page import BasePage
from Tests.acceptance.locators.login_locators import LoginPageLocators
from Tests.acceptance.test_config import *


class LoginPage(BasePage):
    @property
    def url(self):
        return super(LoginPage, self).url + '/account/login'

    @property
    def credential(self):
        return {'email': ACME_CREDENTIAL.get("email"), 'password': decode(ACME_CREDENTIAL.get("password"))}

    @property
    def container_header(self):
        return self.driver.find_element(*LoginPageLocators.CONTAINER_HEADER)



