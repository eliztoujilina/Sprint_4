import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.rental_page_locators import RentalPageLocators

from pages.base_page import BasePage


class RentPage(BasePage):
    def name_field(self):
        return self.browser.find_element(*RentalPageLocators.INPUT_NAME_REGISTER_FORM)

    def last_name_field(self):
        return self.browser.find_element(*RentalPageLocators.LAST_NAME_NAME_REGISTER_FORM)

    def fill_user_data_from(self, family_name):
        self.name_field().send_keys(family_name)

    def address_field(self):
        return self.browser.find_element(*RentalPageLocators.INPUT_ADDRESS_REGISTER_FORM)

    def subway_input(self):
        return self.browser.find_element(*RentalPageLocators.SUBWAY_INPUT)

    def phone_field(self):
        return self.browser.find_element(*RentalPageLocators.INPUT_PHONE_NUMBER_REGISTER_FORM)

    def next_button_rental_page(self):
        return self.browser.find_element(*RentalPageLocators.BUTTON_NEXT_REGISTER_FORM)

    def subway_station_item(self):
        return self.browser.find_element(*RentalPageLocators.SUBWAY_STATION_ITEM)

    def subway_field(self):
        return self.browser.find_element(*RentalPageLocators.SUBWAY_FIELD)

    def date_input(self):
        return self.browser.find_element(*RentalPageLocators.INPUT_DELIVERY_DATE_RENT_FORM)

    def rental_period_item(self):
        return self.browser.find_elements(*RentalPageLocators.RENTAL_PERIOD_ITEM)

    def rental_period_arrow_btn(self):
        return self.browser.find_element(*RentalPageLocators.RENTAL_PERIOD_ARROW_BTN)

    def check_box_color(self):
        return self.browser.find_element(*RentalPageLocators.CHECKBOX_BLACK_COLOR_RENT_FORM)

    def rent_order_btn(self):
        return self.browser.find_element(*RentalPageLocators.RENT_ORDER_BUTTON)

    def yes_confirm_btn(self):
        return self.browser.find_element(*RentalPageLocators.YES_BUTTON_CONFIRM_ORDER_WINDOW)

    def order_finish_text(self):
        return self.browser.find_element(*RentalPageLocators.FINISH_ORDER_MODAL)

    def watch_status_btn(self):
        return self.browser.find_element(*RentalPageLocators.BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW)

    @allure.step("Заполнить данные пользователя в форме аренды")
    def fill_user_data_form(self, name, last_name, address, subway_station="Черкизовская", phone="+89991234567"):
        self.name_field().send_keys(name)
        self.last_name_field().send_keys(last_name)
        self.address_field().send_keys(address)
        self.subway_input().click()
        self.subway_field().send_keys(subway_station)
        self.subway_field().send_keys(Keys.ARROW_DOWN)
        self.subway_field().send_keys(Keys.ENTER)
        self.phone_field().send_keys(phone)
        self.next_button_rental_page().click()

    @allure.step("Заполнить данные даты и времени аренды")
    def fill_ditail_form(self, period):
        self.date_input().click()
        self.date_input().send_keys(Keys.ARROW_RIGHT)
        self.date_input().send_keys(Keys.ENTER)
        self.rental_period_arrow_btn().click()
        self.click_item_in_list(self.rental_period_item(), period)
        self.check_box_color().click()
        self.rent_order_btn().click()
        self.yes_confirm_btn().click()

    @allure.step("Проверить что заказ создан")
    def check_order_finish_text(self):
        assert "Заказ оформлен" in self.order_finish_text().text

    @allure.step("Перейти на страницу статуса заказа")
    def click_watch_status_btn(self):
        self.watch_status_btn().click()






