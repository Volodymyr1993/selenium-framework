from Tests.base import BaseTest
from Pages.SendAgiftPage import SendAgift

class TestSendAgiftFunctional(BaseTest):
    def test_add_product_to_orders(self):
        """
        Test case verify adding first product to orders
        """
        self.send_a_gift = SendAgift(self.driver)

        self.send_a_gift.add_product_to_orders()