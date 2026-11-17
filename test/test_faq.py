import allure
import pytest
from data import BASE_URL, FAQ_ANSWERS
from pages.main_page import MainPage


@allure.feature('Вопросы о важном')
class TestFaq:
    @allure.title('Вопрос FAQ №{index}: отображается соответствующий ответ')
    @pytest.mark.parametrize('index, expected', enumerate(FAQ_ANSWERS), ids=[f'faq-{i + 1}' for i in range(8)])
    def test_question_opens_answer(self, driver, index, expected):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.accept_cookies()
        assert page.expand_question(index) == expected
