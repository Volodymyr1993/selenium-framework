from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class SendAgift(BasePage):
    """ locators - """
    BACK_TO_ORDERS_BUTTON = '//button[@class="LinkButton-sc-1w7z7c2-0 OrderPage__StyledLinkButton-c0eyda-7 bUuaxz ciTiDY"]'
    ORDERS_TITLE = '//h1'
    EDIT_TITLE_BUTTON = '//h1//button[@class="LinkButton-sc-1w7z7c2-0 OrderPage__EditLink-c0eyda-3 bUuaxz keyDUd"]'
    REFRESH_BUTTON = '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM OrderPage__StyledButton-c0eyda-11 jkXxpL"]'
    INVITE_TAB = '//div[@class="Tabs__Container-kudd6e-0 eINFpX"]//div[text()="Invite"]'
    PRODUCTS_TAB = '//div[@class="Tabs__Container-kudd6e-0 eINFpX"]//div[text()="Products"]'
    PRODUCTS_TAB_UPDATE_BUTTON = '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM OrderItems__StyledButton-knh4f6-1 dQpQyg"]'
    PUBLIC_SELECTION_PAGE_TOGGLE = '//div[@class="Toggle__Circle-h1a751-1 cvPdHh"]'
    INVITE_BUTTON = '//button[text()="Invite"]'
    EDIT_BUTTON = '//button[@class="PrimaryButton__Button-sc-1aj0s98-1 bPcAIM GiftNoteConfig__StyledPrimaryButton-kr6bw6-3 fdJGNx"]'

