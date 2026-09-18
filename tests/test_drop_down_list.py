# tests/test_drop_down_list.py
import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from data import Data
from locators import LocatorsQuestions
from helpers import HelpersDropDownList


@allure.feature("Главная страница")
@allure.story("Аккордеон — вопросы о важном")
class TestDropDownList:
    @pytest.mark.parametrize(
        "question_locator, question_name",
        [
            (LocatorsQuestions.QUESTION_FIRST, "Первый вопрос"),
            (LocatorsQuestions.QUESTION_SECOND, "Второй вопрос"),
            (LocatorsQuestions.QUESTION_THIRD, "Третий вопрос"),
            (LocatorsQuestions.QUESTION_FOURTH, "Четвёртый вопрос"),
            (LocatorsQuestions.QUESTION_FIFTH, "Пятый вопрос"),
            (LocatorsQuestions.QUESTION_SIXTH, "Шестой вопрос"),
            (LocatorsQuestions.QUESTION_SEVENTH, "Седьмой вопрос"),
            (LocatorsQuestions.QUESTION_EIGHTH, "Восьмой вопрос"),
        ],
        ids=[
            "first_question",
            "second_question",
            "third_question",
            "fourth_question",
            "fifth_question",
            "sixth_question",
            "seventh_question",
            "eighth_question",
        ],
    )
    @allure.title("Раскрытие аккордеона: {question_name}")
    def test_accordion_item_opens(self, driver: WebDriver, wait, question_locator, question_name):
        driver.get(Data.START_URL)

        element = driver.find_element(*question_locator)

        HelpersDropDownList.click_drop_down_list_element(driver, element, wait)

        expanded_attr = element.get_attribute("aria-expanded")
        assert expanded_attr == "true", (
            f"Аккордеон не раскрылся: {question_name}\n"
            f"Локатор: {question_locator}\n"
            f"Ожидалось aria-expanded='true', получено: '{expanded_attr}'\n"
            f"URL: {driver.current_url}"
        )
