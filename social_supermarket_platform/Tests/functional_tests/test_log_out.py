from Tests.base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData


class TestLogOut(BaseTest):
    def test_verify_log_out(self):
        """
        This test case verify:
         - log out function
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.loginPage.wait_till_loader_disappear()
        self.loginPage.do_log_out()
        self.loginPage.wait_till_loader_disappear()

        assert self.loginPage.is_visible(self.loginPage.LOGIN_TITLE)