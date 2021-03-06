from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''This class is the parent of all Pages'''

class BasePage:
    """ locators - """
    EMAIL_FIELD =  '//input[@id="email"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    LOGIN_BUTTON = '//button[text()="Log In"]'
    LOG_OUT_ICON = '//div[contains(@class, "ProfileMenu__Container-sc")]'
    LOG_OUT_BUTTON = '//button[contains(@class, "LinkButton-sc")]'
    COOKIE_BANNER_DECLINE = '//div[@role="banner"]//a[@id="hs-eu-decline-button"]'
    LOADER = '//div[contains(@class, "Spinner__Overlay-sc-")]'


    def __init__(self, driver, xpath=None, timeout=10):
        self.driver = driver
        self.driver.set_window_size(1920, 1080)
        self.locator = (By.XPATH, xpath)
        self.timeout = timeout

    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator))).click()

    def send_keys(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator))).send_keys(text)

    def get_element_text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element.text

    def is_visible(self, locator, timeout=10):
        """
        An expectation for checking that an element is present on the DOM of a page and visible.
        Visibility means that the element is not only displayed but also has a height and width that is greater than 0.
        locator - used to find the element returns the WebElement once it is located and visible
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return bool(element)

    def get_title(self, title, timeout=10):
        """
        An expectation for checking that the title contains a case-sensitive substring.
        title is the fragment of title expected returns True when the title matches, False otherwise
        """
        WebDriverWait(self.driver, timeout).until(EC.title_contains((By.XPATH, title)))
        return self.driver.title

    def is_clickable(self, locator, timeout=10):
        """
        An Expectation for checking an element is visible and enabled such that you can click it.
        """
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return bool(element)

    def wait_till_loader_disappear(self, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, self.LOADER)))

    # def find_element(self, xpath):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath))
    #     element = WebElement.find_element(xpath)
    #     return element

    # def find_elements(self, xpath):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath))
    #     element = WebElement.find_elements_by_xpath(self.driver, xpath)
    #     return element

    # Login to app
    def do_login(self, username, password):
        self.send_keys(self.EMAIL_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.COOKIE_BANNER_DECLINE)
        self.click(self.LOGIN_BUTTON)
        self.wait_till_loader_disappear()

    # Log out from app
    def do_log_out(self):
        self.click(self.LOG_OUT_ICON)
        self.click(self.LOG_OUT_BUTTON)