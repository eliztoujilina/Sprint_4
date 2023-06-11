from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_CONFIRM_BUTTON = [By.XPATH, "//button[@id='rcc-confirm-button']"]  # кнопка "да все привыкли"
    HEADER_ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g']"]  # кнопка "заказать" в шапке сайта
    MIDDLE_ORDER_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Middle')]"]  # кнопка "заказать" в середине сайта

    LOGO_SCOOTER = [By.XPATH, "//*[@alt='Scooter']"]  # лого самокат в шапке сайта
    LOGO_YANDEX = [By.XPATH, "//*[@alt='Yandex']"]  # лого яндекс в шапке сайта

    QUESTION_1 = [By.XPATH, "//*[@id='accordion__heading-0']"]  # 1-вопрос
    ANSWER_TO_THE_QUESTION_1 = [By.XPATH, "//*[@id='accordion__panel-0']"]  # 1-ответ

    QUESTION_2 = [By.XPATH, "//*[@id='accordion__heading-1']"]  # 2-вопрос
    ANSWER_TO_THE_QUESTION_2 = [By.XPATH, "//*[@id='accordion__panel-1']"]  # 2-ответ

    QUESTION_3 = [By.XPATH, "//*[@id='accordion__heading-2']"]  # 3-вопрос
    ANSWER_TO_THE_QUESTION_3 = [By.XPATH, "//*[@id='accordion__panel-2']"]  # 3-ответ

    QUESTION_4 = [By.XPATH, "//*[@id='accordion__heading-3']"]  # 4-вопрос
    ANSWER_TO_THE_QUESTION_4 = [By.XPATH, "//*[@id='accordion__panel-3']"]  # 4-ответ

    QUESTION_5 = [By.XPATH, "//*[@id='accordion__heading-4']"]  # 5-вопрос
    ANSWER_TO_THE_QUESTION_5 = [By.XPATH, "//*[@id='accordion__panel-4']"]  # 5-ответ

    QUESTION_6 = [By.XPATH, "//*[@id='accordion__heading-5']"]  # 6-вопрос
    ANSWER_TO_THE_QUESTION_6 = [By.XPATH, "//*[@id='accordion__panel-5']"]  # 6-ответ

    QUESTION_7 = [By.XPATH, "//*[@id='accordion__heading-6']"]  # 7-вопрос
    ANSWER_TO_THE_QUESTION_7 = [By.XPATH, "//*[@id='accordion__panel-6']"]  # 7-ответ

    QUESTION_8 = [By.XPATH, "//*[@id='accordion__heading-7']"]  # 8-вопрос
    ANSWER_TO_THE_QUESTION_8 = [By.XPATH, "//*[@id='accordion__panel-7']"]  # 8-ответ