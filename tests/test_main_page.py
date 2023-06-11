import pytest

from Sprint_4.pages.main_page import MainPage
from Sprint_4.data.questions import questions_list


class TestMainPage:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'

    @pytest.mark.parametrize('question, answer', questions_list)
    def test_dropdown_list_questions(self, driver, question, answer):
        main_page = MainPage(driver,  self.MAIN_PAGE_URL)
        main_page.open()
        main_page.check_questions(question=question, answer=answer)
