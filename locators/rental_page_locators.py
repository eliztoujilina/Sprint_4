from selenium.webdriver.common.by import By

class RentalPageLocators:

    INPUT_DELIVERY_DATE_RENT_FORM = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]   # поле ввода даты доставки
    CHANGE_MONTH_BUTTON = [By.XPATH, "//button[@aria-label='Next Month']"]   # кнопка смены месяца в календаре
    CHOOSE_DELIVERY_DATE_NEXT_MONTH_RENT_FORM = [By.XPATH, "//div[@aria-label='Choose вторник, 20-е июня 2023 г.']"]   # выбор даты доставки
    CHOOSE_DELIVERY_DATE_THIS_MONTH_RENT_FORM = [By.XPATH, "//div[@aria-label='Choose вторник, 27-е июня 2023 г.']"]  # выбор даты доставки
    CHOOSE_ARROW_DURATION_RENT_FORM = [By.XPATH, "//span[@class='Dropdown-arrow']"]  # стрелка развернуть список длительности
    CHOOSE_DURATION_1DAY_RENT_FORM = [By.XPATH, "//div[contains(text(), 'сутки')]"]   # выбор длительности аренды 1 сутки
    CHOOSE_DURATION_7DAYS_RENT_FORM = [By.XPATH, "//div[contains(text(), 'семеро суток')]"]  # выбор длительности аренды 7 суток
    CHECKBOX_BLACK_COLOR_RENT_FORM = [By.XPATH, "//label[@for='black']"]   # чекбокс черного цвета самоката
    CHECKBOX_GREY_COLOR_RENT_FORM = [By.XPATH, "//label[@for='grey']"]   # чекбокс серого цвета самоката
    INPUT_COMMENT_RENT_FORM = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]   # поле комментария для курьера
    RENT_FORM_ORDER_BUTTON = [By.XPATH, ".//div[@class='Order_Content__bmtHS']//button[text()='Заказать']"]   # кнопка "Заказать" в футере
    POP_UP_CONFIRM_WINDOW = [By.XPATH, "//div[@class='Order_Form__17u6u']"]  # всплывающее окно подтверждения заказа
    YES_BUTTON_CONFIRM_ORDER_WINDOW = [By.XPATH, "//button[contains(text(), 'Да')]"]  # кнопка "Да" на всплывающем окне подтверждения заказа
    POP_UP_INFO_ORDER_CONFIRMED_WINDOW = [By.XPATH, "//div[@class='Order_Modal__YZ-d3']"]  # вспылвающее окно "Заказ оформлен"
    BUTTON_CHECK_STATUS_POPUP_INFO_WINDOW = [By.XPATH, "//*[contains(text(), 'Посмотреть статус')]"]   # кнопка "Посмотреть статус"