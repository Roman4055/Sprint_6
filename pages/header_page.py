
# pages/header_page.py
from pages.base_page import BasePage
from locators import LocatorsHeader
from selenium.webdriver.support.wait import WebDriverWait

class HeaderPage(BasePage):
    def click_order_button_top(self):
        btn = self.find_element(LocatorsHeader.BTN_ORDER_TOP)
        self.click_js(btn)

    def verify_logo_scooter_visible(self) -> bool:
        logo = self.find_element(LocatorsHeader.LOGO_SCOOTER)
        return logo.is_displayed()

    def go_to_main_via_logo(self):
        logo = self.find_element(LocatorsHeader.LOGO_SCOOTER)
        self.click_js(logo)

    def click_yandex_logo_and_wait_new_tab(self, wait):
        # Клик по логотипу Yandex и ожидание появления второй вкладки
        logo = self.find_element(LocatorsHeader.LOGO_YANDEX)
        # Прокрутка и клик через JS (чтобы избежать ElementClickInterceptedException)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logo)
        self.driver.execute_script("arguments[0].click();", logo)

        # Ждём, что появится вторая вкладка
        wait.until(lambda d: len(d.window_handles) == 2)

    def switch_to_new_tab_and_verify_url(self, wait, expected_domain: str, timeout: int = 20):
        """Переключаемся на новую вкладку и ждём, пока URL будет содержать expected_domain"""
        # Переключаемся на последнюю вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Увеличиваем таймаут специально для этого ожидания
        long_wait = WebDriverWait(self.driver, timeout, poll_frequency=0.5)

        def url_contains_domain(driver):
            url = driver.current_url
            return expected_domain in url and url != "about:blank"

        long_wait.until(url_contains_domain)
        
