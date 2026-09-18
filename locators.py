from selenium.webdriver.common.by import By

class LocatorsQuestions:
    # Заголовки аккордеона (по которым кликаем)
    HEADING_0 = (By.ID, "accordion__heading-0")
    HEADING_1 = (By.ID, "accordion__heading-1")
    HEADING_2 = (By.ID, "accordion__heading-2")
    HEADING_3 = (By.ID, "accordion__heading-3")
    HEADING_4 = (By.ID, "accordion__heading-4")
    HEADING_5 = (By.ID, "accordion__heading-5")
    HEADING_6 = (By.ID, "accordion__heading-6")
    HEADING_7 = (By.ID, "accordion__heading-7")

    # Панели аккордеона (чтобы проверить, что раскрылись)
    PANEL_0 = (By.ID, "accordion__panel-0")
    PANEL_1 = (By.ID, "accordion__panel-1")
    PANEL_2 = (By.ID, "accordion__panel-2")
    PANEL_3 = (By.ID, "accordion__panel-3")
    PANEL_4 = (By.ID, "accordion__panel-4")
    PANEL_5 = (By.ID, "accordion__panel-5")
    PANEL_6 = (By.ID, "accordion__panel-6")
    PANEL_7 = (By.ID, "accordion__panel-7")

class LocatorsOrder:
    BTN_ORDER_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[normalize-space()='Заказать']")
    BTN_ORDER_HOME_DOWN = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[normalize-space()='Заказать']")

    LABEL = (By.CLASS_NAME, 'Order_Header__BZXOb')
    FIELD_NAME = (By.CSS_SELECTOR, "input[placeholder*='Имя']")
    FIELD_SURNAME = (By.CSS_SELECTOR, "input[placeholder*='Фамилия']")
    FIELD_ADDRESS = (By.CSS_SELECTOR, "input[placeholder*='Адрес']")
    FIELD_STATION_METRO = (By.CSS_SELECTOR, "input[placeholder*='Станция метро']")
    FIELD_PHONE = (By.CSS_SELECTOR, "input[placeholder*='Телефон']")
    BTN_NEXT = (By.XPATH, "//button[normalize-space()='Далее']")

    FIELD_WHEN = (By.CSS_SELECTOR, "input[placeholder*='Когда привезти']")
    FIELD_RENTAL_PERIOD = (By.CSS_SELECTOR, "div.Dropdown-control")
    FIELD_RENTAL_PERIOD_VALUE = (By.CSS_SELECTOR, "div.Dropdown-placeholder")

    CHECK_BOXX_BLACK = (By.ID, "black")
    CHECK_BOX_GRAY = (By.ID, "grey")
    FIELD_COMENT = (By.CSS_SELECTOR, "textarea, input[placeholder*='Комментарий']")
    BTN_BACK = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[normalize-space()='Назад']")
    BTN_ORDER_RENT_DOWN = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[normalize-space()='Заказать']")

    MODAL_WINDOW = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
    MODAL_HEADER = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")
    BTN_ORDER_CONFIRM_YES = (By.XPATH, "//button[normalize-space()='Да']")
    BTN_ORDER_CONFIRM_NO = (By.XPATH, "//button[normalize-space()='Нет']")

    MODAL_SUCCESS = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
    MODAL_SUCCESS_HEADER = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")
    MODAL_ORDER_NUMBER_TEXT = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi') and contains(., 'Номер заказа')]")

class LocatorsHeader:
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    BTN_ORDER_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[normalize-space()='Заказать']")
    # НОВЫЙ ЛОКАТОР: логотип Яндекса в шапке
    LOGO_YANDEX = (By.XPATH, "//a[img[@alt='Yandex'] and contains(@href, 'yandex.ru')]")

