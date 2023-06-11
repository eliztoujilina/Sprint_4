from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from Sprint_4.locators.base_page_locators import BasePageLocators


class BasePage:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, browser: webdriver.Chrome, url=MAIN_PAGE_URL, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_visible_element(self, how, what):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((how, what)))

    def move_to_element(self, element):
        webdriver.ActionChains(self.browser).move_to_element(element).perform()

    def scroll_into_view(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def header_yandex_logo(self):
        return self.browser.find_element(*BasePageLocators.LOGO_YANDEX)

    def header_scooter_logo(self):
        return self.browser.find_element(*BasePageLocators.LOGO_SCOOTER)

    def click_item_in_list(self, list_elements, text):
        for element in list_elements:
            if element.text == text:
                self.scroll_into_view(element)
                element.click()
                break
        else:
            raise IndexError(f"Element {text} not exist in list items")

    def url_should_have(self, current_url: str, timeout: int = 5):
        time_spend = 0
        for i in range(timeout):
            if current_url in self.browser.current_url:
                return True
            else:
                if time_spend <= timeout:
                    time_spend += 0.5
                    sleep(0.5)
                else:
                    return False

    def page_should_be_dzen(self):
        self.change_window()
        url = self.browser.current_url
        assert self.url_should_have("dzen.ru")

    def change_window(self):
        wait = WebDriverWait(self.browser, 10)
        original_window_handle = self.browser.current_window_handle
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.browser.window_handles:
            if window_handle != original_window_handle:
                self.browser.switch_to.window(window_handle)
                break

