import pytest
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):
    """ locators - """
    EMAIL_FIELD = '//input[@id="email"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    LOGIN_BUTTON = '//button[text()="Log In"]'
    LOGIN_TITLE = '//h1'
    REGISTER_HERE_LINK = '//a[text()="Register here!"]'
    RESET_PASSWORD_LINK = '//a[text()="Reset Password"]'
    COOKIE_BANNER = '//div[@role="banner"]'
    COOKIE_BANNER_ACCEPT = '//div[@role="banner"]//a[@id="hs-eu-confirmation-button"]'
    COOKIE_BANNER_DECLINE = '//div[@role="banner"]//a[@id="hs-eu-decline-button"]'
    LOG_OUT_ICON = '//div[@class="ProfileMenu__Container-sc-1pvu93g-0 eLDzJI"]'
    LOG_OUT_BUTTON = '//button[@class="LinkButton-sc-1w7z7c2-0 bUuaxz"]'

    ''' Constructor of the page class '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)