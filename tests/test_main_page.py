import allure
import pytest

from pages.main_page import MainPage
from data.questions import questions_list


class TestMainPage:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'

    @pytest.mark.parametrize('question, answer', questions_list)
    @allure.title("Проверить тексты ответов в аккордеоне")
    def test_dropdown_list_questions(self, driver, question, answer):
        main_page = MainPage(driver, self.MAIN_PAGE_URL)
        main_page.open()
        main_page.check_questions(question=question, answer=answer)
