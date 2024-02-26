from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from typing import Tuple


class BasePage:

    def __init__(self, app) -> None:
        self.driver: WebDriver = app.driver

    def presence_element(self, locator, timeout=5):
        """
        Wait for the element at the given locator to be present in the DOM.
        """
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def is_alert_present(self, timeout: int = 5) -> bool:
        """
        Wait for an alert to be present on the page.
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.alert_is_present())
            return True
        except TimeoutException:
            return False

    def wait_for_elements(self, locator, timeout=5):
        """
        Wait for all elements at the given locator to be present in the DOM.
        """
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def type(self, locator: Tuple[str, str], value: str) -> 'BasePage':
        """
        This method types the given value into the field identified by the locator.
        """
        field = self.presence_element(locator)
        current_value_in_field = field.get_attribute('value')
        if current_value_in_field != value:
            field.click()
            if current_value_in_field != '':
                field.clear()
            field.send_keys(value)
        return self
