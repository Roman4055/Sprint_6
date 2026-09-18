# pages/order_page.py
from selenium.webdriver.common.by import By 
from pages.base_page import BasePage
from locators import LocatorsOrder
import time

class OrderPage(BasePage):
    def open_order_form_top_button(self):
        # Клик по верхней кнопке «Заказать» — открывает форму заказа
        btn = self.find_element(LocatorsOrder.BTN_ORDER_TOP)
        self.click_js(btn)
        # Ждём, что форма появилась
        self.find_element(LocatorsOrder.LABEL)

    def fill_personal_info(self, profile):
        self._fill_field(LocatorsOrder.FIELD_NAME, profile.NAME)
        self._fill_field(LocatorsOrder.FIELD_SURNAME, profile.SURNAME)
        self._fill_field(LocatorsOrder.FIELD_ADDRESS, profile.ADDRESS)
        self._fill_field(LocatorsOrder.FIELD_PHONE, profile.PHONE)

    def _fill_field(self, locator, value):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(value)

    def select_metro_station(self, station_name: str):
        input_field = self.find_element(LocatorsOrder.FIELD_STATION_METRO)
        input_field.clear()
        input_field.send_keys(station_name)

        # Ждём появления подсказок
        suggestions_locator = (
            By.XPATH,
            f"//*[contains(@class, 'select-search__option') and contains(., '{station_name}')]"
        )
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        wait = WebDriverWait(self.driver, 15)
        suggestions = wait.until(EC.visibility_of_all_elements_located(suggestions_locator))

        # Обычный клик вместо JS — React лучше его обрабатывает
        suggestions[0].click()

    def set_date(self, date_value: str):
        from selenium.webdriver.common.keys import Keys

        calendar_input = self.find_element(LocatorsOrder.FIELD_WHEN)
        calendar_input.clear()
        calendar_input.send_keys(date_value)

        # Нажимаем Tab — календарь закрывается по потере фокуса
        calendar_input.send_keys(Keys.TAB)

        time.sleep(0.5)

    def select_rental_period(self, period_text: str):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.common.keys import Keys

        wait = WebDriverWait(self.driver, 10)

        # Подстраховка: нажимаем Escape, чтобы закрыть календарь, если он ещё открыт
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.3)

        # Теперь открываем дропдаун
        dropdown = self.find_element(LocatorsOrder.FIELD_RENTAL_PERIOD)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
        dropdown.click()

        time.sleep(0.5)

        option_locator = (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and normalize-space()='{period_text}']"
        )
        option = wait.until(EC.visibility_of_element_located(option_locator))
        option.click()

    def set_checkboxes(self):
        black_cb = self.find_element(LocatorsOrder.CHECK_BOXX_BLACK)
        if not black_cb.is_selected():
            black_cb.click()

        gray_cb = self.find_element(LocatorsOrder.CHECK_BOX_GRAY)
        if not gray_cb.is_selected():
            gray_cb.click()

    def add_comment(self, comment: str):
        comment_field = self.find_element(LocatorsOrder.FIELD_COMENT)
        comment_field.clear()
        comment_field.send_keys(comment)

    def click_next(self):
        btn = self.find_element(LocatorsOrder.BTN_NEXT)
        # Скроллим и кликаем обычным кликом
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()
        # Явно ждём, что вторая часть формы загрузилась
        self.find_element(LocatorsOrder.FIELD_WHEN)
        self.find_element(LocatorsOrder.FIELD_RENTAL_PERIOD)

    def confirm_order(self) -> str:
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.common.by import By

        modal_header = self.find_element(LocatorsOrder.MODAL_HEADER)
        assert "Хотите оформить заказ?" in modal_header.text

        confirm_btn = self.find_element(LocatorsOrder.BTN_ORDER_CONFIRM_YES)
        confirm_btn.click()

        # Ждём, пока текст модалки сменится на «Заказ оформлен»
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda d: "Заказ оформлен" in d.find_element(By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ").text)

        number_text = self.find_element(LocatorsOrder.MODAL_ORDER_NUMBER_TEXT)
        return number_text.text

    def click_order_button(self):
        btn = self.find_element(LocatorsOrder.BTN_ORDER_RENT_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()

