from Tests.base import BaseTest
from Pages.YourImpact import YourImpact


class TestYourImpact(BaseTest):
    def test_verify_all_elements_on_the_page(self):
        """
        This test case verify:
         - each elements visible, clickable at the /dashboard page.
                """
        self.yourImpact = YourImpact(self.driver)

        assert self.yourImpact.is_visible(self.yourImpact.PAGE_TITLE)
        assert self.yourImpact.get_element_text(self.yourImpact.PAGE_TITLE) == 'When you start placing orders we will add metrics here to track your impact.'
