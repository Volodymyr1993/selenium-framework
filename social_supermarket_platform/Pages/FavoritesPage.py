from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class FavouritesPage(BasePage):
    """ locators - """
    FAVORITES_PAGE = '//a[@href="/favorites"]'
    PRODUCT_LIST = '//div[@class="ProductList__Container-jbi448-0 iewNfG"]'
    SEARCH_ICON = '//div[@class="FavoritesPage__Container-sc-1tq5yuv-0 cjtyME"]//i[@class="search icon"][1]'
    FAVORITE_ICON = '//div[@class="FavoritesPage__Container-sc-1tq5yuv-0 cjtyME"]//i[@class="favorite icon"][1]'
    MODAL_CLOSE_BUTTON = '//div[@class="Modal__Close-sc-10kpwz6-4 brEnYU"]'
    MODAL_TITLE = '//h1[@class="ProductModal__Title-sc-18obu0p-4 jMAsjx"]'
    MODAL_DETAILS_BUTTON = '//button[@class="PlainButton-hzadhp-0 AccordionHeader__HeaderButton-sc-33meak-1 boLGoi cOIUGB"]//span[text()="Details"]'
    MODAL_ABOUT_BUTTON = '//button[@class="PlainButton-hzadhp-0 AccordionHeader__HeaderButton-sc-33meak-1 boLGoi cOIUGB"]//span[text()="About "]'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.click(self.FAVORITES_PAGE)
        self.wait_till_loader_disappear()