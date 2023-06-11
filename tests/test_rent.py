from pages.main_page import MainPage
from pages.rent_page import RentPage


class TestRent:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'

    def test_order_buttons_from_header(self, driver):
        main_page = MainPage(driver, self.MAIN_PAGE_URL)
        main_page.open()
        rent_page = main_page.open_rent_page()
        rent_page.fill_user_data_form(name="Тестовое", last_name="Тестовый", address="Тестовый адресс 1")
        rent_page.fill_ditail_form(period="сутки")
        rent_page.check_order_finish_text()

    def test_order_buttons_from_body(self, driver):
        main_page = MainPage(driver, self.MAIN_PAGE_URL)
        main_page.open()
        rent_page = main_page.open_rent_page(from_body=True)
        rent_page.fill_user_data_form(name="Тестовое имя", last_name="Тестовая", address="Тестовый адрес 2")
        rent_page.fill_ditail_form(period="сутки")
        rent_page.check_order_finish_text()

    def test_transit_to_dzen_from_order_history_page(self, driver):
        main_page = MainPage(driver, self.MAIN_PAGE_URL)
        main_page.open()
        rent_page = main_page.open_rent_page(from_body=True)
        rent_page.fill_user_data_form(name="Тестовое имя", last_name="Тестовая", address="Тестовый адрес 2")
        rent_page.fill_ditail_form(period="сутки")
        rent_page.click_watch_status_btn()
        rent_page.header_yandex_logo().click()
        rent_page.page_should_be_dzen()

    def test_transit_to_scooter_page_from_order_history_page(self, driver):
        main_page = MainPage(driver, self.MAIN_PAGE_URL)
        main_page.open()
        rent_page = main_page.open_rent_page(from_body=True)
        rent_page.fill_user_data_form(name="Тестовое имя", last_name="Тестовая", address="Тестовый адрес 2")
        rent_page.fill_ditail_form(period="сутки")
        rent_page.click_watch_status_btn()
        rent_page.header_scooter_logo().click()
        rent_page.url_should_have("https://qa-scooter.praktikum-services.ru/")



