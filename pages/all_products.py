from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class AllProduct(Page):

    ADD_TO_CART = (By.XPATH, "//add-to-cart[@class = 'w-full button button--small' and contains(text(), 'Add to cart')]")
    CHECKOUT = (By.CSS_SELECTOR, "button.button[name = 'checkout']")
    VIEW_CART = (By.CSS_SELECTOR, "a.button.button--secondary")
    PRICES = (By.XPATH, "//div[@class='price__sale']//span[@class= 'price-item price-item--sale']")
    PRODUCT_NAMES = (By.XPATH, "//ul[@id='product-grid']//a/span")

    def verify_all_products(self):
        expected_url = "https://shop.cureskin.com/collections/all"
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    def add_to_cart(self):
        self.driver.first_product_name = self.find_elements(*self.PRODUCT_NAMES)[0].text
        self.driver.price = self.find_elements(*self.PRICES)[0].text
        print(self.driver.first_product_name, self.driver.price)
        first_item = self.find_elements(*self.ADD_TO_CART)[0]
        first_item.click()

    def verify_item_added(self):
        checkout_button = self.wait.until(EC.visibility_of_element_located(self.CHECKOUT))
        assert checkout_button.is_displayed(), "item was not added"

    def click_view_cart(self):
        self.wait_for_element_click(*self.VIEW_CART)

    def verify_product_name(self):
        product_name = self.find_elements(*self.PRODUCT_NAMES)[0].text

