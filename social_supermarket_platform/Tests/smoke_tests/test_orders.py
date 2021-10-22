from Tests.base import BaseTest
from Pages.OrdersPage import OrdersPage

class TestOrdersPage(BaseTest):
    def test_verify_all_elements_at_orders_page_invite_tab(self):
        """
        This test case verify Invite TAB:
         - each elements visible, clickable at Orders page Invite TAB.
         - verify each tab elements is visible, clickable
        """
        self.orders = OrdersPage(self.driver)

        assert self.orders.is_visible(self.orders.ORDERS_CONTAINER)

        # Click at first order to open it
        self.orders.click(self.orders.FIRST_ROW)
        self.orders.wait_till_loader_disappear()

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
        assert self.orders.is_visible(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_ON)
        assert self.orders.is_clickable(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_ON)
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

        # Turn ON toggle to verify publick link is visible
        self.orders.click(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_ON)
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
        self.orders.click(self.orders.PUBLIC_SELECTION_PAGE_TOGGLE_OFF)
        self.orders.wait_till_loader_disappear()

    def test_verify_all_elements_at_orders_page_products_tab(self):
        """
        This test case verify Invite TAB:
         - each elements visible, clickable at Orders page Products TAB.
         - verify each tab elements is visible, clickable
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

    def test_verify_all_elements_at_orders_page_approves_tab(self):
        """
        This test case verify Invite TAB:
         - each elements visible, clickable at Orders page Products TAB.
         - verify each tab elements is visible, clickable
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




