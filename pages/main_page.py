import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Закрыть уведомление о cookies')
    def accept_cookies(self):
        self.click(L.COOKIE_BUTTON)

    @allure.step('Раскрыть вопрос FAQ №{index}')
    def expand_question(self, index):
        self.click(L.question(index))
        return self.visible(L.answer(index)).text

    @allure.step('Начать заказ через кнопку {entry}')
    def start_order(self, entry):
        self.click({'top': L.TOP_ORDER, 'bottom': L.BOTTOM_ORDER}[entry])

    @allure.step('Перейти на главную по логотипу Самоката')
    def click_scooter_logo(self):
        self.click(L.SCOOTER_LOGO)
        self.visible(L.HOME)
        return self.driver.current_url

    @allure.step('Открыть новое окно по логотипу Яндекса')
    def click_yandex_logo(self):
        handles = self.driver.window_handles
        self.click(L.YANDEX_LOGO)
        self.wait.until(EC.new_window_is_opened(handles))
        new_handle = next(h for h in self.driver.window_handles if h not in handles)
        self.driver.switch_to.window(new_handle)
