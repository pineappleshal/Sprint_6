import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from pages.base_page import BasePage


def pytest_addoption(parser):
    parser.addoption('--headed', action='store_true', help='Показать окно Firefox')


@pytest.fixture
def driver(request):
    options = Options()
    if not request.config.getoption('--headed'):
        options.add_argument('-headless')
    if os.getenv('FIREFOX_BINARY'):
        options.binary_location = os.environ['FIREFOX_BINARY']
    service = Service(executable_path=os.environ['GECKODRIVER']) if os.getenv('GECKODRIVER') else Service()
    browser = webdriver.Firefox(options=options, service=service)
    browser.set_window_size(1440, 1000)
    browser.set_page_load_timeout(60)
    try:
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed and 'driver' in item.funcargs:
        page = BasePage(item.funcargs['driver'])
        try:
            allure.attach(page.get_screenshot(), name='Ошибка', attachment_type=allure.attachment_type.PNG)
            allure.attach(page.get_current_url(), name='URL', attachment_type=allure.attachment_type.TEXT)
        except Exception:
            pass  # Ошибка вложения не должна скрыть исходную причину падения.
