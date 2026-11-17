from urllib.parse import urlparse
import allure
from data import BASE_URL
from pages.main_page import MainPage
from pages.dzen_page import DzenPage


@allure.feature('Переходы по логотипам')
class TestNavigation:
    @allure.title('Логотип Самоката возвращает с формы заказа на главную')
    def test_scooter_logo(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL + 'order')
        page.accept_cookies()
        assert page.click_scooter_logo() == BASE_URL

    @allure.title('Логотип Яндекса открывает главную Дзена в новом окне')
    def test_yandex_logo(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.accept_cookies()
        page.click_yandex_logo()
        url = urlparse(DzenPage(driver).wait_for_home())
        assert url.hostname in ('dzen.ru', 'www.dzen.ru')
        assert url.path in ('', '/')
