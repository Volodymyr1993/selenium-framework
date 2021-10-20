from Tests.base import BaseTest
from Pages.SendAgiftPage import SendAgift

class TestSendAgift(BaseTest):
    def test_verify_all_elements_at_send_a_gift_page(self):
        self.send_a_gift = SendAgift(self.driver)

        assert self.send_a_gift.is_visible(self.send_a_gift.PAGE_TITLE)
        assert self.send_a_gift.get_element_text(self.send_a_gift.PAGE_TITLE) == 'Select gifts for them to choose from, all prices include VAT & shipping.'
        assert self.send_a_gift.is_visible(self.send_a_gift.FAVOURITES)
        assert self.send_a_gift.is_clickable(self.send_a_gift.FAVOURITES)
        assert self.send_a_gift.get_element_text(self.send_a_gift.FAVOURITES) == 'FAVOURITES'

        # Verify that each product category is on UI
        list_of_products_from_ui = self.driver.find_elements_by_xpath(self.send_a_gift.OTHER_CATEGORIES)
        for each_product in list_of_products_from_ui:
            assert each_product.text in self.send_a_gift.product_list

        assert self.send_a_gift.is_visible(self.send_a_gift.SEARCH_FOR_A_PRODUCT)
        assert self.send_a_gift.is_clickable(self.send_a_gift.SEARCH_FOR_A_PRODUCT)
        assert self.send_a_gift.is_visible(self.send_a_gift.PRICE_FILTER)
        assert self.send_a_gift.is_clickable(self.send_a_gift.PRICE_FILTER)

        assert self.send_a_gift.is_visible(self.send_a_gift.PLUS_BUTTON)
        assert self.send_a_gift.is_clickable(self.send_a_gift.PLUS_BUTTON)
        assert self.send_a_gift.is_visible(self.send_a_gift.SEARCH_ICON)
        assert self.send_a_gift.is_clickable(self.send_a_gift.SEARCH_ICON)
        assert self.send_a_gift.is_visible(self.send_a_gift.FAVORITE_ICON)
        assert self.send_a_gift.is_clickable(self.send_a_gift.FAVORITE_ICON)
        assert self.send_a_gift.is_visible(self.send_a_gift.LOAD_MORE_BUTTON)
        assert self.send_a_gift.is_clickable(self.send_a_gift.LOAD_MORE_BUTTON)
        assert self.send_a_gift.is_clickable(self.send_a_gift.GO_UP_BUTTON)
        assert self.send_a_gift.is_visible(self.send_a_gift.GO_UP_BUTTON)

        # Click search icon to open modal window
        self.send_a_gift.click(self.send_a_gift.SEARCH_ICON)

        assert self.send_a_gift.is_visible(self.send_a_gift.MODAL_TITLE)
        assert self.send_a_gift.is_visible(self.send_a_gift.MODAL_DROP_DOWN)
        assert self.send_a_gift.is_clickable(self.send_a_gift.MODAL_DROP_DOWN)
        assert self.send_a_gift.is_clickable(self.send_a_gift.MODAL_CLOSE_BUTTON)
        assert self.send_a_gift.is_visible(self.send_a_gift.MODAL_CLOSE_BUTTON)
        assert self.send_a_gift.is_visible(self.send_a_gift.MODAL_DETAILS_BUTTON)
        assert self.send_a_gift.is_clickable(self.send_a_gift.MODAL_DETAILS_BUTTON)
        assert self.send_a_gift.is_clickable(self.send_a_gift.MODAL_ABOUT_BUTTON)
        assert self.send_a_gift.is_visible(self.send_a_gift.MODAL_ABOUT_BUTTON)
        assert self.send_a_gift.is_visible(self.send_a_gift.MODAL_CHOOSE_TYPE_BUTTON)

        # button should be disabled and not clickable TODO method for disabled button
        #assert self.send_a_gift.is_clickable(self.send_a_gift.MODAL_CHOOSE_TYPE_BUTTON)




