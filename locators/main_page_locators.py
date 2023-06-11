from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_CONFIRM_BUTTON = [By.XPATH, "//button[@id='rcc-confirm-button']"]  # кнопка "да все привыкли"
    HEADER_ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g']"]  # кнопка "заказать" в шапке сайта
    MIDDLE_ORDER_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Middle')]"]  # кнопка "заказать" в середине сайта
    ACCORDION_ITEM = (By.XPATH, "//div[@data-accordion-component='AccordionItemHeading']/div") # вопросы
    ANSWER_ITEM = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]") # ответы
    ACCORDION_BLOCK = (By.XPATH, "//div[@class='accordion']") # вопросы блок
