from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Page):

    YOUR_CART = (By.XPATH, "//h1[@class= 'title' and contains(text(), 'Your cart')]")

    def verify_cart_page(self):
        your_cart = self.find_element(*self.YOUR_CART)
        assert your_cart, f"cart page is not displayed"
