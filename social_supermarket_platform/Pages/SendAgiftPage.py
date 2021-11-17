from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class SendAgift(BasePage):
    """ locators - """
    PAGE_TITLE = '//div[contains(@class, "ProductCatalogue__Title-sc-")]'
    SEARCH_FOR_A_PRODUCT = '//input[@type="text"]'
    FAVOURITES = '//button[contains(@class, "CategoryButton__Button-")]'
    OTHER_CATEGORIES = '//button[contains(@class, "CategoryButton__Button-atybu6-0")]'
    PRICE_FILTER = '//div[contains(@class, "PriceFilter__Container-sc-")]'
    LOAD_MORE_BUTTON = '//button[contains(@class, "PrimaryButton__Button-sc-")]'
    GO_UP_BUTTON = '//button[contains(@class, "RoundIconButton__BackTopButton-")]'
    PRODUCTS_LIST = '//div[contains(@class, "ProductList__Products-")]'
    PRODUCT_FROM_LIST = '//div[contains(@class, "ProductCard__Container-")]'
    PLUS_BUTTON = '//i[@class="plus icon"][1]'
    SEARCH_ICON = '//i[@class="search icon"][1]'
    FAVORITE_ICON = '//i[@class="favorite icon"][1]'
    NEXT_BUTTON = '//button[text()="Next"]'
    CONTAINER_WITH_ITEMS = '//div[contains(@class, "ChoiceConfirmationPage__Items-sc")]'
    ORDER_NAME_FIELD = '//input[@id="orderName"]'
    GIFT_NOTE_FIELD = '//textarea[@id="giftNote"]'
    CONFIRM_CHOICES_BUTTON = '//button[text()="Confirm Choices"]'
    BACK_BUTTON = '//button[contains(@class, "LinkButton-sc-1w7z7c2-0 GiftPage__BackButton-")]'

    # Product modal
    MODAL_CLOSE_BUTTON = '//div[contains(@class, "Modal__Close-sc-")]'
    MODAL_TITLE = '//h1[contains(@class, "ProductModal__Title-sc-")]'
    MODAL_DROP_DOWN = '//select[@id="size"]'
    MODAL_WITH_ONE_DROP_DOWN = '//select[contains(@class, "ProductAttributeField__Select-sc")]'
    MODAL_DETAILS_BUTTON = '//button[contains(@class, "PlainButton-")]//span[text()="Details"]'
    MODAL_ABOUT_BUTTON = '//button[contains(@class, "PlainButton-")]//span[text()="About "]'
    MODAL_LET_THEM_CHOOSE_BUTTON = '//button[text()="Let them Choose"]'
    MODAL_CHOOSE_TYPE_BUTTON = '//button[text()="Choose Type"]'
    MODAL_CHOOSE_FIRST_OPTION_FROM_THE_DROP_DOWN = '//div[contains(@class, "ProductAttributeForm__Container-sc-")]//option[2]'

    ''' Constructor of the page class '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_login(TestData.USERNAME, TestData.PASSWORD)

    product_list = ['ACCESSORIES', 'ALCOHOLIC DRINKS', 'BATH & BEAUTY', 'CHRISTMAS HAMPERS & GIFT BOXES', 'CLOTHES',
                    'FOOD', 'GIFT BOXES', 'GIFT SETS', 'HAMPERS', 'HOME & LIVING', 'LETTERBOX GIFTS', 'WELLBEING',
                    'NON-ALCOHOLIC DRINKS']

    def add_product_to_orders(self):
        self.click(self.SEARCH_ICON)
        self.click(self.MODAL_DROP_DOWN)
        self.click(self.MODAL_CHOOSE_FIRST_OPTION_FROM_THE_DROP_DOWN)
        self.click(self.MODAL_CHOOSE_TYPE_BUTTON)
        self.click(self.NEXT_BUTTON)
        self.send_keys(self.ORDER_NAME_FIELD, 'test')
        self.send_keys(self.GIFT_NOTE_FIELD, 'test')
        self.click(self.CONFIRM_CHOICES_BUTTON)
        self.wait_till_loader_disappear()