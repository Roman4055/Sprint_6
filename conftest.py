# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    # Фикстура для запуска и закрытия браузера
    options = Options()

    driver = webdriver.Firefox(options=options)

    # Фиксируем размер окна, чтобы верстка не «ехала» и элементы не перекрывались
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
# Универсальная фикстура WebDriverWait на 10 секунд
    return WebDriverWait(driver, 10)
