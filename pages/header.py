from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):

    SHOP_ALL = (By.XPATH, "//span[@class = 'label' and contains(text(), 'Shop All')]")

    def click_shop_all(self):
        self.click(*self.SHOP_ALL)