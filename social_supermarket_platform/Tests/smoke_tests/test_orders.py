import sys
from Tests.base import BaseTest
from Pages.OrdersPage import OrdersPage
from selenium.common.exceptions import TimeoutException

class TestOrdersPage(BaseTest):
    def test_verify_all_elements_at_orders_page_invite_tab(self):
        """
        This test case verify Invite TAB:
         - each elements visible, clickable at the Orders page --> Invite TAB.
        """
        self.orders = OrdersPage(self.driver)

        assert self.orders.is_visible(self.orders.ORDERS_CONTAINER)

        # Click at first order to open it
        self.orders.click(self.orders.FIRST_ROW)
        self.orders.wait_till_loader_disappear()
        # Verify toggle status before test execution
        self.orders.verify_toggle_status()

        assert self.orders.is_clickable(self.orders.BACK_TO_ORDERS_BUTTON)
        assert self.orders.is_visible(self.orders.BACK_TO_ORDERS_BUTTON)
        assert self.orders.is_visible(self.orders.ORDERS_TITLE)
        assert self.orders.is_visible(self.orders.EDIT_TITLE_BUTTON)
        assert self.orders.is_clickable(self.orders.EDIT_TITLE_BUTTON)
        assert self.orders.is_clickable(self.orders.REFRESH_BUTTON)
        assert self.orders.is_visible(self.orders.REFRESH_BUTTON)
        assert self.orders.is_visible(self.orders.INVITE_TAB)
        assert self.orders.is_clickable(self.orders.INVITE_TAB)
        assert self.orders.is_visible(self.orders.PRODUCTS_TAB)
        assert self.orders.is_clickable(self.orders.PRODUCTS_TAB)
        assert self.orders.is_visible(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_ON)
        assert self.orders.is_clickable(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_ON)
        assert self.orders.is_visible(self.orders.INVITE_BUTTON)
        assert self.orders.is_clickable(self.orders.INVITE_BUTTON)
        assert self.orders.is_visible(self.orders.EDIT_BUTTON)
        assert self.orders.is_clickable(self.orders.EDIT_BUTTON)

        # Click INVITE button to open modal
        self.orders.click(self.orders.INVITE_BUTTON)

        assert self.orders.is_visible(self.orders.INVITE_MODAL)
        assert self.orders.is_visible(self.orders.INVITE_VIA_EMAIL_TITLE)
        assert self.orders.is_visible(self.orders.INVITE_MODAL_CLOSE_BUTTON)
        assert self.orders.is_clickable(self.orders.INVITE_MODAL_CLOSE_BUTTON)
        assert self.orders.is_visible(self.orders.INVITE_MODAL_EMAILS_INPUT)
        assert self.orders.is_clickable(self.orders.INVITE_MODAL_EMAILS_INPUT)
        assert self.orders.is_visible(self.orders.INVITE_MODAL_NEXT_BUTTON)

        # Close INVITE modal
        self.orders.click(self.orders.INVITE_MODAL_CLOSE_BUTTON)

        # Open Gift Note textarea
        self.orders.click(self.orders.EDIT_BUTTON)
        assert self.orders.is_visible(self.orders.SAVE_BUTTON)
        assert self.orders.is_clickable(self.orders.SAVE_BUTTON)
        assert self.orders.is_visible(self.orders.CANSEL_BUTTON)
        assert self.orders.is_clickable(self.orders.CANSEL_BUTTON)

        # Turn ON toggle to verify public link is visible
        self.orders.click(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_ON)
        self.orders.wait_till_loader_disappear()
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK)

        # Open PAge Description text area
        self.orders.click(self.orders.PUBLIC_EDIT_BUTTON)
        assert self.orders.is_visible(self.orders.PUBLIC_SAVE_BUTTON)
        assert self.orders.is_clickable(self.orders.PUBLIC_SAVE_BUTTON)
        assert self.orders.is_visible(self.orders.PUBLIC_CANCEL_BUTTON)
        assert self.orders.is_clickable(self.orders.PUBLIC_CANCEL_BUTTON)
        # turn off the toggle
        self.orders.click(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_OFF)
        self.orders.wait_till_loader_disappear()

    def test_verify_all_elements_at_orders_page_products_tab(self):
        """
        This test case verify Invite TAB:
         - each elements visible, clickable at the Orders page --> Products TAB.
        """
        self.orders = OrdersPage(self.driver)

        # Click at first order to open it
        self.orders.click(self.orders.FIRST_ROW)
        self.orders.wait_till_loader_disappear()

        # Switch to Products tab
        self.orders.click(self.orders.PRODUCTS_TAB)
        self.orders.wait_till_loader_disappear()

        assert self.orders.is_visible(self.orders.PRODUCTS_TAB_PRODUCTS_CONTAINER)
        assert self.orders.is_visible(self.orders.PRODUCTS_TAB_UPDATE_BUTTON)
        assert self.orders.is_visible(self.orders.PRODUCTS_TAB_UPDATE_BUTTON)

    def test_verify_all_elements_at_all_recipients_tab(self):
        """
        This test case verify All Recipients TAB:
         - each elements visible, clickable at the Orders Page --> All Recipients TAB.
        """
        self.orders = OrdersPage(self.driver)

        # Click at first order to open it
        self.orders.click(self.orders.FIRST_ROW)
        self.orders.wait_till_loader_disappear()

        # Click INVITE button to open modal
        self.orders.click(self.orders.INVITE_BUTTON)
        self.orders.wait_till_loader_disappear()

        # input some valid email
        self.orders.send_keys(self.orders.INVITE_MODAL_EMAILS_INPUT, 'test@mail.com')

        # click NEXT button
        self.orders.click(self.orders.INVITE_MODAL_NEXT_BUTTON)

        assert self.orders.is_visible(self.orders.SENDER_NAME_FIELD)
        assert self.orders.is_visible(self.orders.SENDER_NAME_FIELD)
        assert self.orders.is_visible(self.orders.EMAIL_GIFT_MESSAGE)
        assert self.orders.is_clickable(self.orders.EMAIL_GIFT_MESSAGE)
        assert self.orders.is_visible(self.orders.BACK_BUTTON)
        assert self.orders.is_clickable(self.orders.INVITE_VIA_EMAIL_TITLE)
        assert self.orders.is_visible(self.orders.INVITE_VIA_EMAIL_TITLE)

        # Click INVITE button to finish order
        self.orders.click(self.orders.INVITE_MODAL_NEXT_BUTTON)
        self.orders.wait_till_loader_disappear()

        assert self.orders.is_visible(self.orders.ALL_RECIPIENTS_TAB)
        assert self.orders.is_clickable(self.orders.ALL_RECIPIENTS_TAB)
        assert self.orders.is_visible(self.orders.ALL_RECIPIENTS_TABLE)

    def test_verify_all_elements_at_public_selection_page(self):
        """
         - each elements visible, clickable at the Orders --> Public Selection Page.
        """
        self.orders = OrdersPage(self.driver)

        # Click at first order to open it
        self.orders.click(self.orders.FIRST_ROW)
        self.orders.wait_till_loader_disappear()

        # Turn off toggle before test execution
        self.orders.verify_toggle_status()

        # Turn ON toggle click Public link
        self.orders.click(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_ON)
        self.orders.wait_till_loader_disappear()
        self.orders.click(self.orders.PUBLIC_LINK)
        self.orders.wait_till_loader_disappear()

        # Switch to Public Link tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.orders.wait_till_loader_disappear()

        assert self.orders.is_visible(self.orders.PUBLIC_LINK_SUBMIT_BUTTON)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_SUBMIT_BUTTON)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_PHONE_NUMBER_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_PHONE_NUMBER_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_EMAIL_FIELD)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_EMAIL_FIELD)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_FIRST_NAME_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_FIRST_NAME_FIELD)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_LAST_NAME_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_LAST_NAME_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_POSTCODE_FIELD)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_POSTCODE_FIELD)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_ADDRESS1_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_ADDRESS1_FIELD)
        # Click Add Address Line 2 to open the field
        self.orders.click(self.orders.PUBLIC_LINK_ADDRESS2_BUTTON)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_ADDRESS2_FIELD)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_ADDRESS2_FIELD)
        # Click Add Company to open the field
        self.orders.click(self.orders.PUBLIC_LINK_COMPANY_BUTTON)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_COMPANY_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_COMPANY_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_CITY_FIELD)
        assert self.orders.is_clickable(self.orders.PUBLIC_LINK_CITY_FIELD)
        assert self.orders.is_visible(self.orders.PUBLIC_LINK_COUNTRY_FIELD)

        # Close the Public Link browser TAB
        self.driver.close()

        # Switch to Public Link tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # Turn off toggle Public Selection page
        self.orders.verify_toggle_status()

    def test_verify_all_elements_at_pending_approval_tab(self):
        """
        This test case verify Pending Approval TAB:
         - each elements visible, clickable at the Orders Page --> Pending Approval TAB.
        """
        self.orders = OrdersPage(self.driver)

        # Click at first order to open it
        self.orders.click(self.orders.FIRST_ROW)
        self.orders.wait_till_loader_disappear()

        try:
            self.orders.is_clickable(self.orders.PENDING_APPROVAL_TAB, timeout=2)
            # Switch to Pending Approval TAB
            self.orders.click(self.orders.PENDING_APPROVAL_TAB)
            self.orders.wait_till_loader_disappear()
        except:
            TimeoutException

            # Turn off toggle before test execution
            self.orders.verify_toggle_status()
            # add Pending Approval tab
            # Turn ON toggle click Public link
            self.orders.click(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_TURN_ON)
            self.orders.wait_till_loader_disappear()
            self.orders.click(self.orders.PUBLIC_LINK)
            self.orders.wait_till_loader_disappear()

            # Switch to Public Link tab
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.orders.wait_till_loader_disappear()

            # Input all required fields with valid data
            self.orders.send_keys(self.orders.PUBLIC_LINK_PHONE_NUMBER_FIELD, '1234567890')
            self.orders.send_keys(self.orders.PUBLIC_LINK_EMAIL_FIELD, 'test@mail.com')
            self.orders.send_keys(self.orders.PUBLIC_LINK_FIRST_NAME_FIELD, '123456789')
            self.orders.send_keys(self.orders.PUBLIC_LINK_LAST_NAME_FIELD, '123456789')
            self.orders.send_keys(self.orders.PUBLIC_LINK_POSTCODE_FIELD, '123456789')
            self.orders.send_keys(self.orders.PUBLIC_LINK_ADDRESS1_FIELD, '123456789')
            self.orders.send_keys(self.orders.PUBLIC_LINK_CITY_FIELD, '123456789')
            self.orders.click(self.orders.PUBLIC_LINK_SUBMIT_BUTTON)
            self.orders.wait_till_loader_disappear()

            # Switch to Public Link tab
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.orders.wait_till_loader_disappear()

        # Click REFRESH BUTTON
        self.orders.click(self.orders.REFRESH_BUTTON)
        self.orders.wait_till_loader_disappear()

        # Switch to Pending Approval TAB
        self.orders.click(self.orders.PENDING_APPROVAL_TAB)
        self.orders.wait_till_loader_disappear()

        assert self.orders.is_visible(self.orders.PENDING_APPROVAL_TABLE)
        assert self.orders.is_visible(self.orders.PENDING_APPROVAL_APPROVE_BUTTON)
        assert self.orders.is_visible(self.orders.PENDING_APPROVAL_DELETE_BUTTON)

        # Click Select ALL checkbox to verify APPROVE, DELETE buttons are clickable
        self.driver.find_element_by_xpath(self.orders.PENDING_APPROVAL_SELECT_ALL_CHECK_BOX).click()
        assert self.orders.is_clickable(self.orders.PENDING_APPROVAL_APPROVE_BUTTON)
        assert self.orders.is_clickable(self.orders.PENDING_APPROVAL_DELETE_BUTTON)



