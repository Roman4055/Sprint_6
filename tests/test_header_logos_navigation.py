# tests/test_header_logos_navigation.py
import pytest
import allure
from data import Data
from pages.header_page import HeaderPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.feature("Шапка сайта")
@allure.story("Навигация по логотипам")
class TestHeaderLogosNavigation:

    @allure.title("Клик по логотипу Yandex: переход на yandex.ru в новой вкладке")
    def test_click_yandex_logo_redirects_to_yandex(self, driver, wait):
        driver.get(Data.START_URL)

        header = HeaderPage(driver)

        # Клик и ожидание новой вкладки
        header.click_yandex_logo_and_wait_new_tab(wait)

        # Переключение и проверка URL
        header.switch_to_new_tab_and_verify_url(wait, "yandex.ru")

        assert "yandex.ru" in driver.current_url, f"Ожидался yandex.ru, но URL: {driver.current_url}"

    @allure.title("Клик по логотипу Scooter: возврат на главную страницу из другого раздела")
    def test_click_scooter_logo_returns_to_home(self, driver, wait):
        driver.get(Data.START_URL)

        header = HeaderPage(driver)

        # Сначала уходим с главной (кликаем «Заказать» вверху)
        header.click_order_button_top()

        # Убеждаемся, что ушли с главной
        wait.until(lambda d: d.current_url != Data.START_URL)

        # Возвращаемся по логотипу
        header.go_to_main_via_logo()

        # Ждём точного совпадения URL с главной
        wait.until(EC.url_to_be(Data.START_URL))

        assert driver.current_url == Data.START_URL, f"Ожидалась главная страница, но URL: {driver.current_url}"
