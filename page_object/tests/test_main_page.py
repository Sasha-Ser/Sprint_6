import pytest
import allure

from page_object.data import Data #answer_0, answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7
from page_object.pages.main_page import MainPage


class TestMainPage:


    @allure.title('Проверка соответствия вопросу ответа')
    @pytest.mark.parametrize('num, result', [
        (0, Data.answer_0),
        (1, Data.answer_1),
        (2, Data.answer_2),
        (3, Data.answer_3),
        (4, Data.answer_4),
        (5, Data.answer_5),
        (6, Data.answer_6),
        (7, Data.answer_7)])
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result