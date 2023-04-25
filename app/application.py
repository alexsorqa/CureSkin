from pages.base_page import Page
from pages.header import Header
from pages.all_products import AllProduct
from pages.cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.header = Header(self.driver)
        self.all_products = AllProduct(self.driver)
        self.cart_page = CartPage(self.driver)