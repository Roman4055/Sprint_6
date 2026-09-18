# tests/test_order.py
import pytest
import allure
from data import Data, Profile_1, Profile_2
from helpers import HelpersSetProfiles
from locators import LocatorsOrder
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Оформление заказа")
@allure.story("Кнопки «Заказать»")
@pytest.mark.parametrize(
    "button_locator, button_name",
    [
        (LocatorsOrder.BTN_ORDER_TOP, "top_button"),
        (LocatorsOrder.BTN_ORDER_HOME_DOWN, "bottom_button"),
    ],
    ids=["top", "bottom"]
)
class TestOrderButtons:
    @allure.title("Клик по кнопке «Заказать» ({button_name}) — открывается форма")
    def test_click_order_button_opens_form(self, driver, wait, button_locator, button_name):
        driver.get(Data.START_URL)
        button = driver.find_element(*button_locator)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()
        wait.until(EC.visibility_of_element_located(LocatorsOrder.LABEL))
        assert driver.find_element(*LocatorsOrder.LABEL).is_displayed()


@allure.feature("Оформление заказа")
@allure.story("Заполнение формы и подтверждение")
@pytest.mark.parametrize(
    "profile",
    [Profile_1, Profile_2],
    ids=["profile_1_roman", "profile_2_ivan"]
)
class TestOrderForm:
    @allure.title("Полное оформление заказа через верхнюю кнопку (профиль: {profile.NAME})")
    @allure.description(
        "Тест проверяет: заполнение всех полей формы, выбор станции метро, даты, срока аренды, "
        "цвета самоката, комментария; подтверждение заказа и появление окна «Заказ оформлен»."
    )
    def test_fill_full_order_form_top_button(self, driver, wait, profile):
        driver.get(Data.START_URL)
        driver.find_element(*LocatorsOrder.BTN_ORDER_TOP).click()
        wait.until(EC.visibility_of_element_located(LocatorsOrder.LABEL))

        # --- Часть 1 ---
        HelpersSetProfiles.fill_text_fields_part1(driver, wait, profile)
        HelpersSetProfiles.select_metro_station(driver, wait, profile.STATION_METRO)

        assert driver.find_element(*LocatorsOrder.FIELD_NAME).get_attribute("value") == profile.NAME
        assert driver.find_element(*LocatorsOrder.FIELD_SURNAME).get_attribute("value") == profile.SURNAME
        assert driver.find_element(*LocatorsOrder.FIELD_ADDRESS).get_attribute("value") == profile.ADDRESS
        assert driver.find_element(*LocatorsOrder.FIELD_PHONE).get_attribute("value") == profile.PHONE

        # --- Переход на вторую часть ---
        HelpersSetProfiles.click_next_button(driver, wait)
        wait.until(EC.visibility_of_element_located(LocatorsOrder.FIELD_WHEN))
        wait.until(EC.visibility_of_element_located(LocatorsOrder.FIELD_RENTAL_PERIOD))

        # --- Часть 2 ---
        HelpersSetProfiles.fill_text_fields_part2(driver, wait, profile)
        HelpersSetProfiles.set_checkboxes(driver, wait)

        date_value = driver.find_element(*LocatorsOrder.FIELD_WHEN).get_attribute("value")
        assert date_value != "" and date_value is not None, "Поле даты пустое"

        rental_value = driver.find_element(*LocatorsOrder.FIELD_RENTAL_PERIOD_VALUE).text
        assert rental_value == profile.RENTAL_PERIOD

        assert driver.find_element(*LocatorsOrder.FIELD_COMENT).get_attribute("value") == profile.COMMENTS
        assert driver.find_element(*LocatorsOrder.CHECK_BOXX_BLACK).is_selected()
        assert driver.find_element(*LocatorsOrder.CHECK_BOX_GRAY).is_selected()

        # --- Финал ---
        order_btn = driver.find_element(*LocatorsOrder.BTN_ORDER_RENT_DOWN)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_btn)
        order_btn.click()

        HelpersSetProfiles.confirm_order(driver, wait)

        success_text = HelpersSetProfiles.wait_for_success_modal(driver, wait)

        assert "Номер заказа" in success_text, "В сообщении нет номера заказа"
        print(f"✅ Заказ успешно оформлен! Текст: {success_text}")
