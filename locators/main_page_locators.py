from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    TOP_ORDER = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoScooter"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoYandex"]')
    HOME = (By.CSS_SELECTOR, 'div[class*="Home_HomePage"]')

    @staticmethod
    def question(index):
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def answer(index):
        return By.ID, f'accordion__panel-{index}'
