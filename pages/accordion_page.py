# pages/accordion_page.py
from pages.base_page import BasePage
from locators import LocatorsQuestions

class AccordionPage(BasePage):
    def open_question(self, index: int):
        # Открывает вопрос по индексу (0..7)
        heading_locator = getattr(LocatorsQuestions, f"HEADING_{index}")
        panel_locator = getattr(LocatorsQuestions, f"PANEL_{index}")

        heading = self.find_element(heading_locator)
        self.click_js(heading)  # используем клик через JS из BasePage

        # Проверяем, что панель стала видимой
        self.find_element(panel_locator)

    def verify_question_is_open(self, index: int) -> bool:
        # Проверяет, открыт ли вопрос (по наличию aria-expanded='true')
        heading_locator = getattr(LocatorsQuestions, f"HEADING_{index}")
        heading = self.find_element(heading_locator)
        return heading.get_attribute("aria-expanded") == "true"
