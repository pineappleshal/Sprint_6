from datetime import date, timedelta
import allure
import pytest
from data import BASE_URL, ORDERS
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
class TestOrder:
    @allure.title('Успешный заказ самоката: {data[entry]}')
    @pytest.mark.parametrize('data', ORDERS, ids=['top-black-one-day', 'bottom-grey-three-days'])
    def test_successful_order(self, driver, data):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.accept_cookies()
        main.start_order(data['entry'])
        order = OrderPage(driver)
        order.fill_customer(data)
        order.fill_rent(data, (date.today() + timedelta(days=2)).strftime('%d.%m.%Y'))
        order.submit_order()
        assert 'Заказ оформлен' in order.success_message()
