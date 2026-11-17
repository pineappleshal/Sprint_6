from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT = (By.XPATH, "//button[text()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD = (By.CLASS_NAME, 'Dropdown-control')
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM = (By.XPATH, "//button[text()='Да']")
    SUCCESS = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")

    @staticmethod
    def station(name):
        return By.XPATH, f"//button[contains(@class,'Order_SelectOption') and .//div[text()='{name}']]"

    @staticmethod
    def period(label):
        return By.XPATH, f"//div[contains(@class,'Dropdown-option') and text()='{label}']"

    @staticmethod
    def color(color_id):
        return By.ID, color_id
