from Config.config import TestData
from Pages.BasePage import BasePage

class HelpPage(BasePage):
    """ locators - """
    HELP_PAGE = '//a[@href="/guide"]'
    GUIDE_PAGE_HEADING = '//h1[text()="What is This?"]'
    HOW_TO_SEND_A_GIFT = '//h1[text()="How to Send a Gift"]'
    FREQUENTLY_ASKED_QUESTIONS = '//h1[text()="Frequently Asked Questions"]'
    GET_IN_TOUCH = '//h1[text()="Get In Touch"]'

    ''' Constructor of the page class '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.click(self.HELP_PAGE)
        self.wait_till_loader_disappear()