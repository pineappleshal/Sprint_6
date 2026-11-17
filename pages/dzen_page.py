import allure
from pages.base_page import BasePage


class DzenPage(BasePage):
    @allure.step('Дождаться главной страницы Дзена после редиректа')
    def wait_for_home(self):
        return self.wait_for_url_host(('dzen.ru', 'www.dzen.ru'))
