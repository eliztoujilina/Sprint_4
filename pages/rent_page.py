import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RentalFormTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def tearDown(self):
        self.driver.quit()

    def test_rental_form(self):
        # Подтверждение использования куки
        cookie_confirm_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_CONFIRM_BUTTON))
        cookie_confirm_button.click()

        # Нажатие кнопки "Заказать" в шапке сайта
        header_order_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.HEADER_ORDER_BUTTON))
        header_order_button.click()

        # Заполнение полей формы "Для кого самокат"
        input_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.INPUT_NAME_REGISTER_FORM))
        input_name.send_keys("Винсент")

        input_family_name = self.driver.find_element(*RegistrationPageLocators.INPUT_FAMILY_NAME_REGISTER_FORM)
        input_family_name.send_keys("Вангог")

        input_address = self.driver.find_element(*RegistrationPageLocators.INPUT_ADDRESS_REGISTER_FORM)
        input_address.send_keys("Лубянский проезд 15")

        input_metro_station = self.driver.find_element(*RegistrationPageLocators.INPUT_METRO_ST_LIST_REGISTER_FORM)
        input_metro_station.click()

        list_of_metro_stations = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.LIST_OF_METRO_STATIONS_REGISTER_FORM))
        metro_station_option = list_of_metro_stations.find_element(By.XPATH, , 'Бульвар Рокоссовского')]")
        metro_station_option.click()

        input_phone_number = self.driver.find_element(*RegistrationPageLocators.INPUT_PHONE_NUMBER_REGISTER_FORM)
        input_phone_number.send_keys("+79991234567")

        # Нажатие кнопки "Далее"
        button_next = self.driver.find_element(*RegistrationPageLocators.BUTTON_NEXT_REGISTER_FORM)
        button_next.click()

        # Заполнение полей формы "Про аренду"
        input_delivery_date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RentalPageLocators.INPUT_DELIVERY_DATE_RENT_FORM))
        input_delivery_date.click()

        # Выбор даты доставки (в данном случае выбрана дата следующего месяца)
        change_month_button = self.driver.find_element(*RentalPageLocators.CHANGE_MONTH_BUTTON)
        change_month_button.click()

        choose_delivery_date_next_month = self.driver.find_element(
            *RentalPageLocators.CHOOSE_DELIVERY_DATE_NEXT_MONTH_RENT_FORM)
        choose_delivery_date_next_month.click()

        # Выбор длительности аренды (в данном случае выбрана длительность на 7 дней)
        choose_arrow_duration = self.driver.find_element(*RentalPageLocators.CHOOSE_ARROW_DURATION_RENT_FORM)
        choose_arrow_duration.click()

        choose_duration_7days = self.driver.find_element(*RentalPageLocators.CHOOSE_DURATION_7DAYS_RENT_FORM)
        choose_duration_7days.click()

        # Выбор цвета самоката
        checkbox_black_color = self.driver.find_element(*RentalPageLocators.CHECKBOX_BLACK_COLOR_RENT_FORM)
        checkbox_black_color.click()

        # Заполнение комментария для курьера
        input_comment = self.driver.find_element(*RentalPageLocators.INPUT_COMMENT_RENT_FORM)
        input_comment.send_keys("Please deliver to the front door.")

        # Нажатие кнопки "Заказать"
        rent_form_order_button = self.driver.find_element(*RentalPageLocators.RENT_FORM_ORDER_BUTTON)
        rent_form_order_button.click()

        # Проверка всплывающего окна подтверждения заказа
        popup_confirm_window = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RentalPageLocators.POP_UP_CONFIRM_WINDOW))

        # Подтверждение заказа
        yes_button_confirm_order_window = self.driver.find_element(
            *RentalPageLocators.YES_BUTTON_CONFIRM_ORDER_WINDOW)
        yes_button_confirm_order_window.click()

        # Проверка всплывающего окна "Заказ оформлен"
        popup_info_order_confirmed_window = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RentalPageLocators.POP_UP_INFO_ORDER_CONFIRMED_WINDOW))

        # Проверка наличия кнопки "Посмотреть статус"
        button_check_status = self.driver.find_element(*RentalPageLocators.BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW)
        self.assertTrue(button_check_status.is_displayed())


if __name__ == "__main__":
    unittest.main()
