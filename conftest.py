#conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
    

#Фикстура запуска/закрытия браузера
@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    d = webdriver.Firefox(options=options)
    yield d
    d.quit()

