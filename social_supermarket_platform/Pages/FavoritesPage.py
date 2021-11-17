from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class FavouritesPage(BasePage):
    """ locators - """
    FAVORITES_PAGE = '//a[@href="/favorites"]'
    PRODUCT_LIST = '//div[contains(@class, "ProductList__Container")]'
    SEARCH_ICON = '//div[contains(@class, "FavoritesPage__Container-sc")]//i[@class="search icon"][1]'
    FAVORITE_ICON = '//div[contains(@class, "FavoritesPage__Container-sc-")]//i[@class="favorite icon"][1]'
    MODAL_CLOSE_BUTTON = '//div[contains(@class, "Modal__Close-sc-")]'
    MODAL_TITLE = '//h1[contains(@class, "ProductModal__Title-sc-")]'
    MODAL_DETAILS_BUTTON = '//button[contains(@class, "PlainButton")]//span[text()="Details"]'
    MODAL_ABOUT_BUTTON = '//button[contains(@class, "PlainButton")]//span[text()="About "]'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.click(self.FAVORITES_PAGE)
        self.wait_till_loader_disappear()