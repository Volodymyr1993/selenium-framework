from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class SendAgift(BasePage):
    """ locators - """
    PAGE_TITLE = '//div[@class="ProductCatalogue__Title-sc-1kai38p-3 kmefkK"]'
    SEARCH_FOR_A_PRODUCT = '//input[@type="text"]'
    FAVOURITES = '//button[@class="CategoryButton__Button-atybu6-0 kKZNSc"]'
    OTHER_CATEGORIES = '//button[@class="CategoryButton__Button-atybu6-0 igAitb"]'
    PRICE_FILTER = '//div[@class="PriceFilter__Container-sc-1ip33kp-0 coSEZl"]'
    LOAD_MORE_BUTTON = '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM"]'
    GO_UP_BUTTON = '//button[@class="RoundIconButton__BackTopButton-uci0o1-0 hwnGi"]'
    PRODUCTS_LIST = '//div[@class="ProductList__Products-jbi448-2 kzUUHv"]'
    PRODUCT_FROM_LIST = '//div[@class="ProductCard__Container-pavi5k-0 dCgtmR"]'
    PLUS_BUTTON = '//i[@class="plus icon"][1]'
    SEARCH_ICON = '//i[@class="search icon"][1]'
    FAVORITE_ICON = '//i[@class="favorite icon"][1]'