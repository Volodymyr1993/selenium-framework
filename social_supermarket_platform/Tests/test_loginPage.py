import Config.config
from Tests.base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData


class TestLogin(BaseTest):
    def test_verify_all_elements_on_the_page(self):
        self.loginPage = LoginPage(self.driver)

        # Verify elements are visible at the page
        assert self.loginPage.is_visible(self.loginPage.EMAIL_FIELD)
        assert self.loginPage.is_visible(self.loginPage.PASSWORD_FIELD)
        assert self.loginPage.is_visible(self.loginPage.COOKIE_BANNER)
        assert self.loginPage.is_visible(self.loginPage.LOGIN_BUTTON)
        assert self.loginPage.is_visible(self.loginPage.REGISTER_HERE_LINK)
        assert self.loginPage.is_visible(self.loginPage.RESET_PASSWORD_LINK)
        assert self.loginPage.is_visible(self.loginPage.COOKIE_BANNER)
        assert self.loginPage.is_visible(self.loginPage.COOKIE_BANNER_ACCEPT)
        assert self.loginPage.is_visible(self.loginPage.COOKIE_BANNER_DECLINE)

        # Verify if buttons and links are clickable
        assert self.loginPage.is_clickable(self.loginPage.EMAIL_FIELD)
        assert self.loginPage.is_clickable(self.loginPage.PASSWORD_FIELD)
        assert self.loginPage.is_clickable(self.loginPage.COOKIE_BANNER)
        assert self.loginPage.is_clickable(self.loginPage.LOGIN_BUTTON)
        assert self.loginPage.is_clickable(self.loginPage.REGISTER_HERE_LINK)
        assert self.loginPage.is_clickable(self.loginPage.RESET_PASSWORD_LINK)
        assert self.loginPage.is_clickable(self.loginPage.COOKIE_BANNER)
        assert self.loginPage.is_clickable(self.loginPage.COOKIE_BANNER_ACCEPT)
        assert self.loginPage.is_clickable(self.loginPage.COOKIE_BANNER_DECLINE)




    # def test_login(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)