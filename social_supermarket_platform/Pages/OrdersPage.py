from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class OrdersPage(BasePage):
    """ locators - """
    ORDERS_PAGE = '//a[@href="/orders"]'
    ORDERS_CONTAINER = '//div[@class="OrdersPage__Container-sc-7h779g-0 bJlzXY"]'
    BACK_TO_ORDERS_BUTTON = '//button[@class="LinkButton-sc-1w7z7c2-0 OrderPage__StyledLinkButton-c0eyda-7 bUuaxz ciTiDY"]'
    ORDERS_TITLE = '//h1'
    FIRST_ROW = '//div[@class="ag-center-cols-container"]//div[@row-id="0"]'
    EDIT_TITLE_BUTTON = '//h1//button[@class="LinkButton-sc-1w7z7c2-0 OrderPage__EditLink-c0eyda-3 bUuaxz keyDUd"]'
    REFRESH_BUTTON = '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM OrderPage__StyledButton-c0eyda-11 jkXxpL"]'
    INVITE_TAB = '//div[@class="Tabs__Container-kudd6e-0 eINFpX"]//div[text()="Invite"]'
    PUBLIC_SELECTION_PAGE_TOGGLE_TURN_ON = '//div[@class="Toggle__Circle-h1a751-1 cvPdHh"]'
    PUBLIC_SELECTION_PAGE_TOGGLE_TURN_OFF = '//div[@class="Toggle__Circle-h1a751-1 NhBDC"]'
    INVITE_BUTTON = '//button[text()="Invite"]'
    EDIT_BUTTON = '//div[@class="GiftNoteConfig__Container-kr6bw6-0 kIlZrQ"]//button[text()="Edit"]'
    SAVE_BUTTON = '//div[@class="GiftNoteConfig__Container-kr6bw6-0 kIlZrQ"]//button[text()="Save"]'
    CANSEL_BUTTON = '//div[@class="GiftNoteConfig__Container-kr6bw6-0 kIlZrQ"]//button[text()="Cancel"]'
    GIFT_NOTE_TEXTAREA = '//textarea[@class="GiftNoteConfig__Textarea-kr6bw6-6 kaNWjr"]'

    # Public Selection Page section
    PUBLIC_LINK = '//div[@class="ShareableSelectionPageConfig__Url-dp8gek-4 JDsqx"]//a'
    PUBLIC_EDIT_BUTTON = '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM ShareableSelectionPageConfig__StyledPrimaryButton-dp8gek-10 kYGMvC"]'
    PUBLIC_SAVE_BUTTON = '//form[@class="ShareableSelectionPageConfig__DescriptionForm-dp8gek-8 Jjjhe"]//button[text()="Save"]'
    PUBLIC_CANCEL_BUTTON = '//form[@class="ShareableSelectionPageConfig__DescriptionForm-dp8gek-8 Jjjhe"]//button[text()="Cancel"]'
    PUBLIC_TEXTAREA_BUTTON = '//form[@class="ShareableSelectionPageConfig__DescriptionForm-dp8gek-8 Jjjhe"]//textarea'

    # Invite via Email modal
    INVITE_MODAL = '//div[@class="Modal__Content-sc-10kpwz6-1 gOFxnS"]'
    INVITE_VIA_EMAIL_TITLE = '//div[@class="Modal__Content-sc-10kpwz6-1 gOFxnS"]//h1'
    INVITE_MODAL_CLOSE_BUTTON = '//div[@class="Modal__Content-sc-10kpwz6-1 gOFxnS"]//div[@class="Modal__Close-sc-10kpwz6-4 brEnYU"]'
    INVITE_MODAL_EMAILS_INPUT = '//div[@class="Modal__Content-sc-10kpwz6-1 gOFxnS"]//textarea[@class="InviteByEmailModal__Textarea-dnhv5e-4 FLAlr"]'
    INVITE_MODAL_NEXT_BUTTON = '//div[@class="Modal__Content-sc-10kpwz6-1 gOFxnS"]//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM InviteByEmailModal__StyledButton-dnhv5e-8 khOlvR"]'

    # Products tab
    PRODUCTS_TAB_PRODUCTS_CONTAINER = '//div[@class="OrderItems__Container-knh4f6-0 hUfEtj"]'
    PRODUCTS_TAB = '//div[@class="Tabs__Container-kudd6e-0 eINFpX"]//div[text()="Products"]'
    PRODUCTS_TAB_UPDATE_BUTTON = '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM OrderItems__StyledButton-knh4f6-1 dQpQyg"]'

    # Ivvite view Email second tab
    SENDER_NAME_FIELD = '//input[@id="senderName"]'
    EMAIL_GIFT_MESSAGE = '//textarea[@id="emailGiftMessage"]'
    BACK_BUTTON = '//button[text()="Back"]'
    INVITE_VIEA_EMAIL_INVITE_BUTTON = '//button[text()="INVITE"]'

    # All Recipients TAB
    ALL_RECIPIENTS_TAB = '//div[@class="Tabs__Button-kudd6e-3 ebKLBX"]'
    ALL_RECIPIENTS_TABLE = '//div[@class="ResponseList__Container-dhrcr0-0 gtArHw ag-theme-alpine"]'

    # Pending Approval TAB
    PENDING_APPROVAL_TAB = '//div[@class="Tabs__Button-kudd6e-3 ebKLBX"]'
    PENDING_APPROVAL_APPROVE_BUTTON = '//button[text()="Approve"]'
    PENDING_APPROVAL_DELETE_BUTTON = '//button[text()="Delete"]'
    PENDING_APPROVAL_TABLE = '//div[@class="ResponseList__Container-dhrcr0-0 gtArHw ag-theme-alpine"]'
    PENDING_APPROVAL_SELECT_ALL_CHECK_BOX = '//div[@role="columnheader"]//input[@class="ag-input-field-input ag-checkbox-input"][0]'
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
        if self.is_visible(self.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_OFF):
            self.click(self.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_OFF)
        elif self.is_visible(self.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_ON):
            pass


