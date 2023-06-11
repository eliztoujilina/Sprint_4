from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_4.pages.base_page import BasePage
from Sprint_4.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def accordion_items(self):
        return self.browser.find_elements(*MainPageLocators.ACCORDION_ITEM)

    def answer_item(self):
        return self.find_visible_element(*MainPageLocators.ANSWER_ITEM)

    def accordion_block(self):
        return self.browser.find_element(*MainPageLocators.ACCORDION_BLOCK)

    def rent_page_btn(self):
        return self.browser.find_element(*MainPageLocators.HEADER_ORDER_BUTTON)

    def from_body_rent_page_btn(self):
        return self.browser.find_element(*MainPageLocators.MIDDLE_ORDER_BUTTON)

    def check_questions(self, question: str, answer: str):
        self.scroll_into_view(self.accordion_block())
        self.click_item_in_list(self.accordion_items(), question)
        assert self.answer_item().text == answer

    def open_rent_page(self, from_body=False):
        from Sprint_4.pages.rent_page import RentPage
        if from_body:
            self.scroll_into_view(self.from_body_rent_page_btn())
            self.from_body_rent_page_btn().click()
        else:
            self.rent_page_btn().click()
        return RentPage(self.browser)



