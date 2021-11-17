from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.color import Color

class OrdersPage(BasePage):
    """ locators - """
    ORDERS_PAGE = '//a[@href="/orders"]'
    ORDERS_CONTAINER = '//div[contains(@class, "OrdersPage__Container-sc")]'
    BACK_TO_ORDERS_BUTTON = '//button[contains(@class, "LinkButton-sc-1w7z7c2-0 fDqHbc")]'
    ORDERS_TITLE = '//h1'
    FIRST_ROW = '//div[@class="ag-center-cols-container"]//div[@row-id="0"]'
    EDIT_TITLE_BUTTON = '//h1//button[contains(@class, "LinkButton-sc-1w7z7c2-0 OrderPage__EditLink-")]'
    REFRESH_BUTTON = '//button[contains(text(), "Refresh")]'
    INVITE_TAB = '//div[contains(@class, "Tabs__Container")]//div[text()="Invite"]'
    PUBLIC_SELECTION_PAGE_TOGGLE = '//div[contains(@class, "Toggle__Container-sc")]'
    # PUBLIC_SELECTION_PAGE_TOGGLE_TURN_OFF = '//div[contains(@class, "Toggle__Circle-h1a751-1")]'
    INVITE_BUTTON = '//button[text()="Invite"]'
    EDIT_BUTTON = '//div[contains(@class, "GiftNoteConfig__Container")]//button[text()="Edit"]'
    SAVE_BUTTON = '//div[contains(@class, "GiftNoteConfig__Container")]//button[text()="Save"]'
    CANSEL_BUTTON = '//div[contains(@class, "GiftNoteConfig__Container")]//button[text()="Cancel"]'
    GIFT_NOTE_TEXTAREA = '//textarea[contains(@class, "GiftNoteConfig__Textarea")]'

    # Public Selection Page section
    PUBLIC_LINK = '//div[contains(@class, "ShareableSelectionPageConfig__Url")]//a'
    PUBLIC_EDIT_BUTTON = '//button[contains(@class, "PrimaryButton__Button-sc-1aj0s98-1 fEIcqn ShareableSelectionPage")]'
    PUBLIC_SAVE_BUTTON = '//form[contains(@class, "ShareableSelectionPageConfig__DescriptionForm-")]//button[text()="Cancel"]'
    PUBLIC_CANCEL_BUTTON = '//form[contains(@class, "ShareableSelectionPageConfig__DescriptionForm-")]//button[text()="Cancel"]'
    PUBLIC_TEXTAREA_BUTTON = '//form[contains(@class, "ShareableSelectionPageConfig__DescriptionForm-")]//textarea'

    # Invite via Email modal
    INVITE_MODAL = '//div[contains(@class, "Modal__Content-sc")]'
    INVITE_VIA_EMAIL_TITLE = '//div[contains(@class, "Modal__Content-sc")]//h1'
    INVITE_MODAL_CLOSE_BUTTON = '//div[contains(@class, "Modal__Content-sc-10kpwz6-1")]//div[contains(@class, "Modal__Close-sc-")]'
    INVITE_MODAL_EMAILS_INPUT = '//div[contains(@class, "Modal__Content-sc-10kpwz6-1")]//textarea[contains(@class, "InviteByEmailModal__Textarea")]'
    INVITE_MODAL_NEXT_BUTTON = '//div[contains(@class, "Modal__Content-sc-10kpwz6-1")]//button[contains(@class, "PrimaryButton__Button-sc")]'

    # Products tab
    PRODUCTS_TAB_PRODUCTS_CONTAINER = '//div[contains(@class, "OrderItems__Container-")]'
    PRODUCTS_TAB = '//div[contains(@class, "Tabs__Container")]//div[text()="Products"]'
    PRODUCTS_TAB_UPDATE_BUTTON = '//button[contains(@class, "PrimaryButton__Button-sc-1aj0s98-1 fEIcqn OrderItems__StyledButton-sc")]'

    # Ivvite view Email second tab
    SENDER_NAME_FIELD = '//input[@id="senderName"]'
    EMAIL_GIFT_MESSAGE = '//textarea[@id="emailGiftMessage"]'
    BACK_BUTTON = '//button[text()="Back"]'
    INVITE_VIEA_EMAIL_INVITE_BUTTON = '//button[text()="INVITE"]'

    # All Recipients TAB
    ALL_RECIPIENTS_TAB = '//div[contains(@class, "Tabs__Container")]//div[contains(text(), "All Recipients")]'
    ALL_RECIPIENTS_TABLE = '//div[contains(@class, "ResponseList__Container-sc")]'

    # Pending Approval TAB
    PENDING_APPROVAL_TAB = '//*[contains(text(), "Pending Approval")]'
    PENDING_APPROVAL_APPROVE_BUTTON = '//button[text()="Approve"]'
    PENDING_APPROVAL_DELETE_BUTTON = '//button[text()="Delete"]'
    PENDING_APPROVAL_TABLE = '//div[contains(@class, "Tabs__Container")]//div[contains(text(), "Pending Approval")]'
    PENDING_APPROVAL_SELECT_ALL_CHECK_BOX = '//input[@class="ag-input-field-input ag-checkbox-input"]'
    PENDING_APPROVAL_FIRST_CHECK_BOX_FROM_THE_LIST = '//div[@class="ag-center-cols-container"]//div[@role="row"]//input'

    # Publick Link separate page elements
    PUBLIC_LINK_TITLE = '//h1'
    PUBLIC_LINK_PHONE_NUMBER_FIELD = '//input[@id="phone"]'
    PUBLIC_LINK_EMAIL_FIELD = '//input[@id="email"]'
    PUBLIC_LINK_FIRST_NAME_FIELD = '//input[@id="firstName"]'
    PUBLIC_LINK_LAST_NAME_FIELD = '//input[@id="lastName"]'
    PUBLIC_LINK_POSTCODE_FIELD = '//input[@id="postCode"]'
    PUBLIC_LINK_ADDRESS1_FIELD = '//input[@id="address1"]'
    PUBLIC_LINK_ADDRESS2_BUTTON = '//button[text()="Add Address Line 2"]'
    PUBLIC_LINK_ADDRESS2_FIELD = '//input[@id="address2"]'
    PUBLIC_LINK_COMPANY_FIELD = '//input[@id="company"]'
    PUBLIC_LINK_COMPANY_BUTTON = '//button[text()="Add Company"]'
    PUBLIC_LINK_CITY_FIELD = '//input[@id="city"]'
    PUBLIC_LINK_COUNTRY_FIELD = '//input[@id="country"]'
    PUBLIC_LINK_SUBMIT_BUTTON = '//button[text()="Submit"]'



    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.click(self.ORDERS_PAGE)
        self.wait_till_loader_disappear()

    def verify_toggle_status(self):
        """
        Method to verify the toggle status. In case toggle is turned on before test case we should turn it off.
        If toggle is turned off - pass
        :return:
        """
        element_color = self.driver.find_element_by_xpath(
            self.PUBLIC_SELECTION_PAGE_TOGGLE).value_of_css_property('background-color')
        hex = Color.from_string(element_color).hex
        try:
            if hex == '#008000':  # Green
                self.click(self.PUBLIC_SELECTION_PAGE_TOGGLE, timeout=1)
        except TimeoutException:
            pass



