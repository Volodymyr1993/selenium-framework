import pytest
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):
    """ locators - """
    EMAIL_FIELD = (By.XPATH, '//input[@id="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Log In"]')
    LOGIN_TITLE = (By.XPATH, '//h1')
    REGISTER_HERE_LINK = (By.XPATH, '//a[text()="Register here!"]')
    RESET_PASSWORD_LINK = (By.XPATH, '//a[text()="Reset Password"]')
    COOKIE_BANNER = (By.XPATH, '//div[@role="banner"]')
    COOKIE_BANNER_ACCEPT = (By.XPATH, '//div[@role="banner"]//a[@id="hs-eu-confirmation-button"]')
    COOKIE_BANNER_DECLINE = (By.XPATH, '//div[@role="banner"]//a[@id="hs-eu-decline-button"]')
    LOG_OUT_ICON = (By.XPATH, '//div[@class="ProfileMenu__Container-sc-1pvu93g-0 eLDzJI"]')
    LOG_OUT_BUTTON = (By.XPATH, '//button[@class="LinkButton-sc-1w7z7c2-0 bUuaxz"]')

    ''' Constructor of the page class '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Login to app
    def do_login(self, username, password):
        self.send_keys(self.EMAIL_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    # Log out from app
    def do_log_out(self):
        self.click(self.LOG_OUT_ICON)
        self.click(self.LOGIN_BUTTON)