from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class RegisterPage(BasePage):
    """ locators - """
    FIRST_NAME_FIELD = '//input[@id="firstName"]'
    LAST_NAME_FIELD = '//input[@id="lastName"]'
    EMAIL_FIELD = '//input[@id="email"]'
    COMPANY_FIELD = '//input[@id="company"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    REGISTER_BUTTON = '//button[contains(@class, "PrimaryButton__Button-sc-")]'
    GO_BACK_BUTTON = '//a[text()="Go Back"]'
    REGISTER_TITLE = '//h1'
    COOKIE_BANNER = '//div[@role="banner"]'
    COOKIE_BANNER_ACCEPT = '//div[@role="banner"]//a[@id="hs-eu-confirmation-button"]'
    COOKIE_BANNER_DECLINE = '//div[@role="banner"]//a[@id="hs-eu-decline-button"]'

    ''' Constructor of the page class '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.REGISTER_LINK)


