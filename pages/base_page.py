# pages/base_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        # visibility — элемент виден и готов к взаимодействию
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_js(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_invisibility(self, locator, timeout=10):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator),
                            message=f"Элемент {locator} не исчез за {timeout} сек")
        except TimeoutException:
            pass
