from Tests.base import BaseTest
from Pages.PasswordResetPage import PasswordResetPage

class TestPasswordReset(BaseTest):
    def test_verify_all_elements_on_the_register_page(self):
        """
        This test case verify:
         - each elements visible, clickable /passwordReset page.
        """
        self.passwordReset = PasswordResetPage(self.driver)

        # Verify elements are visible at the page
        assert self.passwordReset.is_visible(self.passwordReset.EMAIL_FIELD)
        assert self.passwordReset.is_visible(self.passwordReset.RESET_PASSWORD_BUTTON)
        assert self.passwordReset.is_visible(self.passwordReset.GO_BACK_BUTTON)
        assert self.passwordReset.is_visible(self.passwordReset.COOKIE_BANNER)
        assert self.passwordReset.is_visible(self.passwordReset.COOKIE_BANNER_ACCEPT)
        assert self.passwordReset.is_visible(self.passwordReset.COOKIE_BANNER_DECLINE)

        # Verify text is correct
        assert self.passwordReset.get_element_text(self.passwordReset.RESET_PASSWORD_TITLE) == 'Reset Password'

        # Verify if buttons and links are clickable
        assert self.passwordReset.is_clickable(self.passwordReset.EMAIL_FIELD)
        assert self.passwordReset.is_clickable(self.passwordReset.RESET_PASSWORD_BUTTON)
        assert self.passwordReset.is_clickable(self.passwordReset.GO_BACK_BUTTON)
        assert self.passwordReset.is_clickable(self.passwordReset.COOKIE_BANNER)
        assert self.passwordReset.is_clickable(self.passwordReset.COOKIE_BANNER_ACCEPT)
        assert self.passwordReset.is_clickable(self.passwordReset.COOKIE_BANNER_DECLINE)

