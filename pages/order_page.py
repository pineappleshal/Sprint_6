import allure
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators as L
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнить данные получателя')
    def fill_customer(self, data):
        for locator, key in [(L.NAME, 'name'), (L.SURNAME, 'surname'),
                             (L.ADDRESS, 'address'), (L.PHONE, 'phone')]:
            self.fill(locator, data[key])
        self.fill(L.METRO, data['metro'])
        self.click(L.station(data['metro']))
        self.click(L.NEXT)

    @allure.step('Заполнить данные аренды')
    def fill_rent(self, data, delivery_date):
        self.fill(L.DATE, delivery_date)
        self.visible(L.DATE).send_keys(Keys.ENTER)
        self.click(L.PERIOD)
        self.click(L.period(data['period']))
        self.click(L.color(data['color']))
        self.fill(L.COMMENT, data['comment'])

    @allure.step('Подтвердить заказ')
    def submit_order(self):
        self.click(L.ORDER)
        self.click(L.CONFIRM)

    @allure.step('Прочитать сообщение об успешном заказе')
    def success_message(self):
        return self.visible(L.SUCCESS).text
