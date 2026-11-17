from urllib.parse import urlparse

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step('Открыть страницу {url}')
    def open(self, url):
        self.driver.get(url)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        element = self.visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.visible(locator).text

    def send_keys(self, locator, *keys):
        self.visible(locator).send_keys(*keys)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_host(self, hosts):
        self.wait.until(lambda driver: urlparse(driver.current_url).hostname in hosts)
        return self.get_current_url()

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_new_window(self, previous_handles):
        self.wait.until(EC.new_window_is_opened(previous_handles))
        new_handle = next(handle for handle in self.get_window_handles()
                          if handle not in previous_handles)
        self.driver.switch_to.window(new_handle)

    def get_screenshot(self):
        return self.driver.get_screenshot_as_png()
