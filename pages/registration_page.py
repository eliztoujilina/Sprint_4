import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationFormTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def tearDown(self):
        self.driver.quit()

    def test_registration_form(self):
        # Подтверждение использования куки
        cookie_confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.COOKIE_CONFIRM_BUTTON))
        cookie_confirm_button.click()

        # Нажатие кнопки "Заказать" в шапке сайта
        header_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.HEADER_ORDER_BUTTON))
        header_order_button.click()

        # Заполнение полей формы
        input_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.INPUT_NAME_REGISTER_FORM))
        input_name.send_keys("Винсент")

        input_family_name = self.driver.find_element(*RegistrationPageLocators.INPUT_FAMILY_NAME_REGISTER_FORM)
        input_family_name.send_keys("Вангог")

        input_address = self.driver.find_element(*RegistrationPageLocators.INPUT_ADDRESS_REGISTER_FORM)
        input_address.send_keys("Лубянский проезд 15")

        input_metro_station = self.driver.find_element(*RegistrationPageLocators.INPUT_METRO_ST_LIST_REGISTER_FORM)
        input_metro_station.click()

        list_of_metro_stations = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.LIST_OF_METRO_STATIONS_REGISTER_FORM))
        metro_station_option = list_of_metro_stations.find_element(By.XPATH, , 'Бульвар Рокоссовского')]")
        metro_station_option.click()

        input_phone_number = self.driver.find_element(*RegistrationPageLocators.INPUT_PHONE_NUMBER_REGISTER_FORM)
        input_phone_number.send_keys("+79991234567")

        # Нажатие кнопки "Далее"
        button_next = self.driver.find_element(*RegistrationPageLocators.BUTTON_NEXT_REGISTER_FORM)
        button_next.click()

        # Проверка перехода на следующую страницу (предполагается, что проверка будет продолжена на следующих шагах)
        assert "https://qa-scooter.praktikum-services.ru/next-page" in self.driver.current_url

        if __name__ == "__main__":
            unittest.main()
