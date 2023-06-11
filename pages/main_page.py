from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sprint_4.locators.main_page_locators import MainPageLocators

class MainPage:
    def open(self):
        pass

    def tearDown(self):
        self.driver.quit()

    def test_main_page(self):
        # Подтверждение использования куки
        cookie_confirm_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_CONFIRM_BUTTON))
        cookie_confirm_button.click()

        # Проверка наличия логотипов
        assert self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).is_displayed()
        assert self.driver.find_element(*MainPageLocators.LOGO_YANDEX).is_displayed()

        # Проверка открытия ответов на вопросы
        questions = [
            (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_TO_THE_QUESTION_1),
            (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_TO_THE_QUESTION_2),
            (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_TO_THE_QUESTION_3),
            (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_TO_THE_QUESTION_4),
            (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_TO_THE_QUESTION_5),
            (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_TO_THE_QUESTION_6),
            (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_TO_THE_QUESTION_7),
            (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_TO_THE_QUESTION_8)
        ]

        for question, answer in questions:
            question_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(question))
            question_element.click()

            answer_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(answer))
            assert answer_element.is_displayed()

    def test_order_button(self):
        # Подтверждение использования куки
        cookie_confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.COOKIE_CONFIRM_BUTTON))
        cookie_confirm_button.click()

        # Проверка кнопки "Заказать" в шапке сайта
        header_order_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.HEADER_ORDER_BUTTON))
        header_order_button.click()

        # Проверка наличия формы заказа
        assert "https://qa-scooter.praktikum-services.ru/rent" in self.driver.current_url
        assert self.driver.find_element(*RentalFormLocators.NAME_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.PHONE_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.EMAIL_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.ADDRESS_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.SUBMIT_BUTTON).is_displayed()

        # Возвращение на главную страницу
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

        # Проверка кнопки "Заказать" в середине сайта
        middle_order_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MIDDLE_ORDER_BUTTON))
        middle_order_button.click()

        # Проверка наличия формы заказа
        assert "https://qa-scooter.praktikum-services.ru/rent" in self.driver.current_url
        assert self.driver.find_element(*RentalFormLocators.NAME_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.PHONE_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.EMAIL_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.ADDRESS_INPUT).is_displayed()
        assert self.driver.find_element(*RentalFormLocators.SUBMIT_BUTTON).is_displayed()
