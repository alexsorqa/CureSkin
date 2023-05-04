from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.all_products import AllProduct
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Page):

    YOUR_CART = (By.XPATH, "//h1[@class= 'title' and contains(text(), 'Your cart')]")
    CART_PRODUCT_NAME = (By.XPATH, "//tr[@class= 'cart-item']//a[@class= 'cart-item__name link']")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, "td.cart-item__prices.small-hide.right span.price.price--end price-money bdi")
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, ".cart-item__name.link")
    PRODUCT_PRICE_CART = (By.CSS_SELECTOR, ".price.price--end bdi")

    def verify_cart_page(self):
        your_cart = self.find_element(*self.YOUR_CART)
        assert your_cart, f"cart page is not displayed"

    def verify_name_and_price(self):
        actual_product_name = self.wait_for_element_appear(*self.CART_PRODUCT_NAME).text
        actual_product_price = self.wait_for_element_appear(*self.PRODUCT_PRICE_CART).text

        assert actual_product_name == self.driver.first_product_name, f'Expected {self.driver.first_product_name} but got {actual_product_name}'
        assert actual_product_price == self.driver.price, f'Expected {self.driver.price} but got {actual_product_price}'


