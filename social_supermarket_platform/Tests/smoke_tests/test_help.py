from Tests.base import BaseTest
from Pages.HelpPage import HelpPage


class TestHelp(BaseTest):
    def test_verify_all_elements_on_the_help_page(self):
        """
        This test case verify:
         - each elements visible, clickable at the Help page.
                """
        self.helpPage = HelpPage(self.driver)

        assert self.helpPage.is_visible(self.helpPage.GUIDE_PAGE_HEADING)
        assert self.helpPage.is_visible(self.helpPage.HOW_TO_SEND_A_GIFT)
        assert self.helpPage.is_visible(self.helpPage.FREQUENTLY_ASKED_QUESTIONS)
        assert self.helpPage.is_visible(self.helpPage.GET_IN_TOUCH)

        assert self.helpPage.get_element_text(self.helpPage.GUIDE_PAGE_HEADING) == 'What is This?'
        assert self.helpPage.get_element_text(self.helpPage.HOW_TO_SEND_A_GIFT) == 'How to Send a Gift'
        assert self.helpPage.get_element_text(self.helpPage.FREQUENTLY_ASKED_QUESTIONS) == 'Frequently Asked Questions'
        assert self.helpPage.get_element_text(self.helpPage.GET_IN_TOUCH) == 'Get In Touch'