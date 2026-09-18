# tests/test_order.py
import pytest
import allure
from data import Data, Profile_1, Profile_2
from pages.order_page import OrderPage
from locators import LocatorsOrder
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Оформление заказа")
@allure.story("Кнопки «Заказать»")
@pytest.mark.parametrize(
    "button_locator, button_name",
    [
        (LocatorsOrder.BTN_ORDER_TOP, "верхняя"),
        (LocatorsOrder.BTN_ORDER_HOME_DOWN, "нижняя"),
    ],
    ids=["top_button", "bottom_button"]
)
class TestOrderButtons:
    @allure.title("Клик по кнопке «Заказать» ({button_name}) — открывается форма")
    def test_click_order_button_opens_form(self, driver, wait, button_locator, button_name):
        driver.get(Data.START_URL)

        # Скроллим и кликаем обычным кликом
        button = driver.find_element(*button_locator)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

        # Ждём, что форма появилась
        wait.until(EC.visibility_of_element_located(LocatorsOrder.LABEL))
        assert driver.find_element(*LocatorsOrder.LABEL).is_displayed()


@allure.feature("Оформление заказа")
@allure.story("Заполнение формы заказа")
class TestOrder:
    @pytest.mark.parametrize(
        "profile",
        [Profile_1, Profile_2],
        ids=["profile_1_roman", "profile_2_ivan"]
    )
    @allure.title("Успешное оформление заказа ({profile.NAME})")
    def test_successful_order(self, driver, profile):
        driver.get(Data.START_URL)

        order = OrderPage(driver)

        # Сначала открываем форму!
        order.open_order_form_top_button()

        order.fill_personal_info(profile)
        order.select_metro_station(profile.STATION_METRO)
        order.click_next()

        order.set_date(profile.WHEN)
        order.select_rental_period(profile.RENTAL_PERIOD)
        order.add_comment(profile.COMMENTS)
        order.set_checkboxes()

        # Кнопка «Заказать» в форме (нижняя)
        order.click_order_button()

        order_number = order.confirm_order()
        assert "Номер заказа" in order_number
