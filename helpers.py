# helpers.py
import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import LocatorsOrder


class HelpersDropDownList:
    @staticmethod
    @allure.step("Клик по элементу аккордеона")
    def click_drop_down_list_element(driver, element, wait):
        # Прокручиваем элемент в видимую область
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        
        # Ждём, что элемент станет кликабельным (на случай, если он ещё не готов)
        wait.until(EC.element_to_be_clickable(element))
        
        # Клик через JS — игнорирует перекрывающие элементы (картинку)
        driver.execute_script("arguments[0].click();", element)

class HelpersSetProfiles:
    @staticmethod
    @allure.step("Заполнение текстовых полей — часть 1 (имя, фамилия, адрес, телефон)")
    def fill_text_fields_part1(driver, wait, profile):
        fields = [
            (LocatorsOrder.FIELD_NAME, profile.NAME),
            (LocatorsOrder.FIELD_SURNAME, profile.SURNAME),
            (LocatorsOrder.FIELD_ADDRESS, profile.ADDRESS),
            (LocatorsOrder.FIELD_PHONE, profile.PHONE),
        ]
        for locator, value in fields:
            field = wait.until(EC.element_to_be_clickable(locator))
            field.clear()
            field.send_keys(value)

    @staticmethod
    @allure.step("Выбор станции метро: {station_name}")
    def select_metro_station(driver, wait, station_name):
        input_field = wait.until(
            EC.element_to_be_clickable(LocatorsOrder.FIELD_STATION_METRO)
        )
        input_field.clear()
        input_field.send_keys(station_name)

        wait.until(EC.presence_of_all_elements_located((
            By.XPATH,
            "//*[contains(@class, 'select-search__option')]"
        )))

        suggestion_locator = (
            By.XPATH,
            f"//*[contains(@class, 'select-search__option') and contains(., '{station_name}')]"
        )

        suggestion = wait.until(EC.element_to_be_clickable(suggestion_locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", suggestion)
        suggestion.click()

    @staticmethod
    @allure.step("Выбор даты через календарь: {date_iso}")
    def set_date_via_calendar(driver, wait, locator, date_iso):
        months_ru = {
            1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
            5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
            9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
        }

        parts = date_iso.split('-')
        year_i = int(parts[0])
        month_i = int(parts[1])
        day_i = int(parts[2])

        field = wait.until(EC.element_to_be_clickable(locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", field)
        field.click()

        wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "div.react-datepicker__day"
        )))

        month_name = months_ru[month_i]
        search_text = f"{day_i}-е {month_name} {year_i}"

        cell_locator = (
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day') and contains(@aria-label, '{search_text}')]"
        )

        try:
            cell = driver.find_element(*cell_locator)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cell)
            cell.click()
            return
        except Exception:
            pass

        next_btn_locator = (By.CSS_SELECTOR, "div.react-datepicker__navigation--next")

        for _ in range(12):
            try:
                next_btn = wait.until(EC.element_to_be_clickable(next_btn_locator))
                next_btn.click()
                time.sleep(0.5)
            except Exception:
                break

            try:
                cell = driver.find_element(*cell_locator)
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cell)
                cell.click()
                return
            except Exception:
                continue

        raise Exception(f"Не удалось найти дату {date_iso} в календаре")

    @staticmethod
    @allure.step("Выбор срока аренды: {period_text}")
    def select_rental_period(driver, wait, period_text):
        field = wait.until(EC.element_to_be_clickable(LocatorsOrder.FIELD_RENTAL_PERIOD))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", field)
        field.click()

        option_locator = (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and normalize-space()='{period_text}']"
        )

        option = wait.until(EC.element_to_be_clickable(option_locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        option.click()

    @staticmethod
    @allure.step("Заполнение текстовых полей — часть 2 (дата, срок, комментарий)")
    def fill_text_fields_part2(driver, wait, profile):
        HelpersSetProfiles.set_date_via_calendar(
            driver, wait, LocatorsOrder.FIELD_WHEN, profile.WHEN
        )
        HelpersSetProfiles.select_rental_period(driver, wait, profile.RENTAL_PERIOD)

        comment_field = wait.until(EC.element_to_be_clickable(LocatorsOrder.FIELD_COMENT))
        comment_field.clear()
        comment_field.send_keys(profile.COMMENTS)

    @staticmethod
    @allure.step("Установка чекбоксов: чёрный и серый цвет")
    def set_checkboxes(driver, wait):
        black_cb = wait.until(EC.element_to_be_clickable(LocatorsOrder.CHECK_BOXX_BLACK))
        if not black_cb.is_selected():
            black_cb.click()

        gray_cb = wait.until(EC.element_to_be_clickable(LocatorsOrder.CHECK_BOX_GRAY))
        if not gray_cb.is_selected():
            gray_cb.click()

    @staticmethod
    @allure.step("Нажатие кнопки «Далее»")
    def click_next_button(driver, wait):
        next_btn = wait.until(EC.element_to_be_clickable(LocatorsOrder.BTN_NEXT))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
        next_btn.click()

    @staticmethod
    @allure.step("Заполнение всей формы заказа")
    def fill_full_order_form(driver, wait, profile):
        HelpersSetProfiles.fill_text_fields_part1(driver, wait, profile)
        HelpersSetProfiles.select_metro_station(driver, wait, profile.STATION_METRO)

        HelpersSetProfiles.click_next_button(driver, wait)

        wait.until(EC.visibility_of_element_located(LocatorsOrder.FIELD_WHEN))
        wait.until(EC.visibility_of_element_located(LocatorsOrder.FIELD_RENTAL_PERIOD))

        HelpersSetProfiles.fill_text_fields_part2(driver, wait, profile)
        HelpersSetProfiles.set_checkboxes(driver, wait)

    @staticmethod
    @allure.step("Подтверждение заказа в модальном окне")
    def confirm_order(driver, wait):
        modal_window = wait.until(EC.visibility_of_element_located(LocatorsOrder.MODAL_WINDOW))

        header_text = modal_window.find_element(*LocatorsOrder.MODAL_HEADER).text
        assert "Хотите оформить заказ?" in header_text, f"Неверный заголовок модального окна: {header_text}"

        confirm_btn = wait.until(EC.element_to_be_clickable(LocatorsOrder.BTN_ORDER_CONFIRM_YES))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_btn)
        confirm_btn.click()

    @staticmethod
    @allure.step("Ожидание модального окна «Заказ оформлен»")
    def wait_for_success_modal(driver, wait):
        success_text_el = wait.until(
            EC.visibility_of_element_located(LocatorsOrder.MODAL_ORDER_NUMBER_TEXT)
        )

        header = driver.find_element(*LocatorsOrder.MODAL_SUCCESS_HEADER)
        assert "Заказ оформлен" in header.text, f"Неверный заголовок: {header.text}"

        return success_text_el.text
