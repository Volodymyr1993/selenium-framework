from Tests.base import BaseTest
from Pages.RegisterPage import RegisterPage

class TestRegisterPage(BaseTest):
    def test_verify_all_elements_on_the_register_page(self):
        """
        This test case verify:
         - each elements visible, clickable /register page.
        """
        self.registerPage = RegisterPage(self.driver)

        # Verify elements are visible at the page
        assert self.registerPage.is_visible(self.registerPage.FIRST_NAME_FIELD)
        assert self.registerPage.is_visible(self.registerPage.LAST_NAME_FIELD)
        assert self.registerPage.is_visible(self.registerPage.EMAIL_FIELD)
        assert self.registerPage.is_visible(self.registerPage.COMPANY_FIELD)
        assert self.registerPage.is_visible(self.registerPage.PASSWORD_FIELD)
        assert self.registerPage.is_visible(self.registerPage.REGISTER_BUTTON)
        assert self.registerPage.is_visible(self.registerPage.GO_BACK_BUTTON)
        assert self.registerPage.is_visible(self.registerPage.COOKIE_BANNER)
        assert self.registerPage.is_visible(self.registerPage.COOKIE_BANNER_ACCEPT)
        assert self.registerPage.is_visible(self.registerPage.COOKIE_BANNER_DECLINE)
        assert self.registerPage.is_visible(self.registerPage.REGISTER_TITLE)

        # Verify text is correct
        assert self.registerPage.get_element_text(self.registerPage.REGISTER_TITLE) == 'Register'

        # Verify if buttons and links are clickable
        assert self.registerPage.is_clickable(self.registerPage.FIRST_NAME_FIELD)
        assert self.registerPage.is_clickable(self.registerPage.LAST_NAME_FIELD)
        assert self.registerPage.is_clickable(self.registerPage.EMAIL_FIELD)
        assert self.registerPage.is_clickable(self.registerPage.COMPANY_FIELD)
        assert self.registerPage.is_clickable(self.registerPage.PASSWORD_FIELD)
        assert self.registerPage.is_clickable(self.registerPage.REGISTER_BUTTON)
        assert self.registerPage.is_clickable(self.registerPage.GO_BACK_BUTTON)
        assert self.registerPage.is_clickable(self.registerPage.COOKIE_BANNER)
        assert self.registerPage.is_clickable(self.registerPage.COOKIE_BANNER_ACCEPT)
        assert self.registerPage.is_clickable(self.registerPage.COOKIE_BANNER_DECLINE)

