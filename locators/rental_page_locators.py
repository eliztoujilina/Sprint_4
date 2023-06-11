from selenium.webdriver.common.by import By

class RentalPageLocators:

    INPUT_DELIVERY_DATE_RENT_FORM = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]   # поле ввода даты доставки
    CHANGE_MONTH_BUTTON = [By.XPATH, "//button[@aria-label='Next Month']"]   # кнопка смены месяца в календаре
    RENTAL_PERIOD_ARROW_BTN = [By.XPATH, "//span[@class='Dropdown-arrow']"]  # стрелка развернуть список длительности
    CHECKBOX_BLACK_COLOR_RENT_FORM = [By.XPATH, "//label[@for='black']"]   # чекбокс черного цвета самоката
    CHECKBOX_GREY_COLOR_RENT_FORM = [By.XPATH, "//label[@for='grey']"]   # чекбокс серого цвета самоката
    INPUT_COMMENT_RENT_FORM = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]   # поле комментария для курьера
    RENT_ORDER_BUTTON = [By.XPATH, ".//div[@class='Order_Content__bmtHS']//button[text()='Заказать']"]   # кнопка "Заказать" в футере
    POP_UP_CONFIRM_WINDOW = [By.XPATH, "//div[@class='Order_Form__17u6u']"]  # всплывающее окно подтверждения заказа
    YES_BUTTON_CONFIRM_ORDER_WINDOW = [By.XPATH, "//button[contains(text(), 'Да')]"]  # кнопка "Да" на всплывающем окне подтверждения заказа
    POP_UP_INFO_ORDER_CONFIRMED_WINDOW = [By.XPATH, "//div[@class='Order_Modal__YZ-d3']"]  # вспылвающее окно "Заказ оформлен"
    BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW = [By.XPATH, "//*[contains(text(), 'Посмотреть статус')]"]   # кнопка "Посмотреть статус"
    INPUT_NAME_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Имя']"]  # поле ввода имени
    LAST_NAME_NAME_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Фамилия']"]  # поле ввода фамилии
    INPUT_ADDRESS_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]  # поле ввода адреса
    SUBWAY_INPUT = [By.XPATH, "//div[@class='select-search']"]  # поле выбора станции метро
    INPUT_PHONE_NUMBER_REGISTER_FORM = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]  # поле ввода телефона
    BUTTON_NEXT_REGISTER_FORM = [By.XPATH, "//button[contains(text(), 'Далее')]"]  # кнопка "Далее" под формой регистрации
    SUBWAY_STATION_ITEM = (By.XPATH, "//input[@class='select-search__select']") # поле метро
    SUBWAY_FIELD = (By.XPATH, "//input[@class='select-search__input']")  # список станций метро
    RENTAL_PERIOD_ITEM = (By.XPATH, "//div[@class='Dropdown-option']") # срок аренды
    FINISH_ORDER_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']") # завершение бронирования