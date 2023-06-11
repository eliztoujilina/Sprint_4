from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_SCOOTER = [By.XPATH, "//*[@alt='Scooter']"]  # лого самокат в шапке сайта
    LOGO_YANDEX = [By.XPATH, "//*[@alt='Yandex']"]  # лого яндекс в шапке сайта