from urllib.parse import urlparse
import allure
from pages.base_page import BasePage


class DzenPage(BasePage):
    @allure.step('Дождаться главной страницы Дзена после редиректа')
    def wait_for_home(self):
        self.wait.until(lambda d: urlparse(d.current_url).hostname in ('dzen.ru', 'www.dzen.ru'))
        return self.driver.current_url
