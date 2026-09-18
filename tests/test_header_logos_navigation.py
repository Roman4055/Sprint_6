# tests/test_header_logos_navigation.py
import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import Data
from locators import LocatorsHeader

@allure.feature("Шапка сайта")
@allure.story("Навигация по логотипам")
class TestHeaderLogosNavigation:

    @allure.title("Клик по логотипу Yandex: переход на yandex.ru в новой вкладке")
    def test_click_yandex_logo_redirects_to_yandex(self, driver, wait):
        driver.get(Data.START_URL)

        wait.until(EC.presence_of_element_located(LocatorsHeader.LOGO_SCOOTER))

        logo = wait.until(EC.visibility_of_element_located(LocatorsHeader.LOGO_YANDEX))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logo)
        driver.execute_script("arguments[0].click();", logo)

        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])

        # Ждём, пока URL в новой вкладке загрузится (Firefox сначала показывает about:blank)
        wait.until(EC.url_contains("yandex.ru"))

        assert "yandex.ru" in driver.current_url, f"Ожидался yandex.ru, но URL: {driver.current_url}"



    @allure.title("Клик по логотипу Scooter: возврат на главную страницу из другого раздела")
    def test_click_scooter_logo_returns_to_home(self, driver, wait):
        driver.get(Data.START_URL)

        order_btn = wait.until(EC.element_to_be_clickable(LocatorsHeader.BTN_ORDER_TOP))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_btn)
        order_btn.click()

        # Убеждаемся, что ушли с главной (URL не равен START_URL)
        wait.until(lambda d: d.current_url != Data.START_URL)

        logo = wait.until(EC.element_to_be_clickable(LocatorsHeader.LOGO_SCOOTER))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logo)
        logo.click()

        # Ждём, пока URL станет точно равен START_URL
        wait.until(EC.url_to_be(Data.START_URL))

        assert driver.current_url == Data.START_URL, f"Ожидалась главная страница, но URL: {driver.current_url}"
