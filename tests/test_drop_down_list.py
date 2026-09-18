# tests/test_drop_down_list.py
import pytest
import allure
from pages.accordion_page import AccordionPage
from data import Data

@allure.feature("Главная страница")
@allure.story("Аккордеон — вопросы о важном")
class TestDropDownList:
    @pytest.mark.parametrize(
        "index, question_name",
        [
            (0, "Первый вопрос"),
            (1, "Второй вопрос"),
            (2, "Третий вопрос"),
            (3, "Четвёртый вопрос"),
            (4, "Пятый вопрос"),
            (5, "Шестой вопрос"),
            (6, "Седьмой вопрос"),
            (7, "Восьмой вопрос"),
        ],
        ids=[
            "first_question", "second_question", "third_question",
            "fourth_question", "fifth_question", "sixth_question",
            "seventh_question", "eighth_question"
        ]
    )
    @allure.title("Раскрытие аккордеона: {question_name}")
    def test_accordion_item_opens(self, driver, index, question_name):
        driver.get(Data.START_URL)

        accordion = AccordionPage(driver)
        accordion.open_question(index)

        assert accordion.verify_question_is_open(index), f"Аккордеон не раскрылся: {question_name}"
