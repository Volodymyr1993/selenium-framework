from Tests.base import BaseTest
from Pages.FavoritesPage import FavouritesPage

class TestFavorites(BaseTest):
    def test_verify_all_elements_at_favorites_page(self):
        """
        This test case verify:
         - each elements visible, clickable at Favorites page.
         - each element in product modal is visible, clickable
        """
        self.favorites = FavouritesPage(self.driver)

        assert self.favorites.is_visible(self.favorites.PRODUCT_LIST)
        assert self.favorites.is_visible(self.favorites.SEARCH_ICON)
        assert self.favorites.is_clickable(self.favorites.SEARCH_ICON)
        assert self.favorites.is_clickable(self.favorites.FAVORITE_ICON)
        assert self.favorites.is_visible(self.favorites.FAVORITE_ICON)

        # click SEARCH_ICON to open modal
        self.favorites.click(self.favorites.SEARCH_ICON)

        assert self.favorites.is_visible(self.favorites.MODAL_TITLE)
        assert self.favorites.is_visible(self.favorites.MODAL_DETAILS_BUTTON)
        assert self.favorites.is_clickable(self.favorites.MODAL_DETAILS_BUTTON)
        assert self.favorites.is_visible(self.favorites.MODAL_ABOUT_BUTTON)
        assert self.favorites.is_clickable(self.favorites.MODAL_ABOUT_BUTTON)
        assert self.favorites.is_clickable(self.favorites.MODAL_CLOSE_BUTTON)
        assert self.favorites.is_visible(self.favorites.MODAL_CLOSE_BUTTON)
