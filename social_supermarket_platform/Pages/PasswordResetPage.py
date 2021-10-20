from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class PasswordResetPage(BasePage):
    """ locators - """
    EMAIL_FIELD = (By.XPATH, '//input[@id="email"]')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM"]')
    GO_BACK_BUTTON = (By.XPATH, '//a[text()="Go Back"]')
    RESET_PASSWORD_TITLE = (By.XPATH, '//h1')
    COOKIE_BANNER = (By.XPATH, '//div[@role="banner"]')
    COOKIE_BANNER_ACCEPT = (By.XPATH, '//div[@role="banner"]//a[@id="hs-eu-confirmation-button"]')
    COOKIE_BANNER_DECLINE = (By.XPATH, '//div[@role="banner"]//a[@id="hs-eu-decline-button"]')

    ''' Constructor of the page class '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.RESET_PASSWORD_LINK)


