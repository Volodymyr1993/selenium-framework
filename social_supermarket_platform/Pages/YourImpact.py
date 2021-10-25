from Config.config import TestData
from Pages.BasePage import BasePage

class YourImpact(BasePage):
    """ locators - """
    YOUR_IMPACT_PAGE = '//a[@href="/dashboard"]'
    PAGE_TITLE = '//div[@class="Placeholder__Container-sc-1am38zg-0 koVThv"]'

    ''' Constructor of the page class '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.click(self.YOUR_IMPACT_PAGE)
        self.wait_till_loader_disappear()