from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import BaseWebDriver, WebDriver
from selenium.webdriver.remote.webelement import WebElement

'''This class is the parent of all Pages'''

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_window_size(1920, 1080)

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        """
        An expectation for checking that an element is present on the DOM of a page and visible.
        Visibility means that the element is not only displayed but also has a height and width that is greater than 0.
        locator - used to find the element returns the WebElement once it is located and visible
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_title(self, title):
        """
        An expectation for checking that the title contains a case-sensitive substring.
        title is the fragment of title expected returns True when the title matches, False otherwise
        """
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        return self.driver.title

    def is_clickable(self, by_locator):
        """
        An Expectation for checking an element is visible and enabled such that you can click it.
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def find_element(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath))
        element = WebElement(self.driver).find_element_by_xpath(xpath)
        return element