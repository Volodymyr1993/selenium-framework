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

    # Product modal
    MODAL_CLOSE_BUTTON = '//div[@class="Modal__Close-sc-10kpwz6-4 brEnYU"]'
    MODAL_TITLE = '//h1[@class="ProductModal__Title-sc-18obu0p-4 jMAsjx"]'
    MODAL_DROP_DOWN = '//div[@class="ProductAttributeForm__Container-sc-912fkl-0 cPHjyt"]'
    MODAL_DETAILS_BUTTON = '//button[@class="PlainButton-hzadhp-0 AccordionHeader__HeaderButton-sc-33meak-1 boLGoi cOIUGB"]'
    MODAL_ABOUT_BUTTON = '//div[@class="AccordionHeader__ArrowContainer-sc-33meak-2 jVbFZJ"][1]'
    MODAL_LET_THEM_CHOOSE_BUTTON = '//button[text()="Let them Choose"]'
    MODAL_CHOOSE_TYPE_BUTTON = '//button[text()="Choose Type"]'

    ''' Constructor of the page class '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_login(TestData.USERNAME, TestData.PASSWORD)

    product_list = ['ACCESSORIES', 'ALCOHOLIC DRINKS', 'BATH & BEAUTY', 'CHRISTMAS HAMPERS & GIFT BOXES', 'CLOTHES',
                    'FOOD', 'GIFT BOXES', 'GIFT SETS', 'HAMPERS', 'HOME & LIVING', 'LETTERBOX GIFTS', 'WELLBEING',
                    'NON-ALCOHOLIC DRINKS']