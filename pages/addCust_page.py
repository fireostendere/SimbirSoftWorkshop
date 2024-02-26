import allure

from selenium.webdriver.common.by import By
from typing import Tuple, Union

from pages.base_page import BasePage


class AddCustPage(BasePage):
    """
    This class represents the Add Customer Page and contains methods to interact with it.
    """

    # Locators
    _FIRST_NAME: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(1) > .form-control')
    _LAST_NAME: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(2) > .form-control')
    _POST_CODE: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(3) > .form-control')
    _ADD_CUSTOMER_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '.btn-default')

    @allure.step('fill customer form with first name: {first_name}, last name: {last_name}, and postcode: {postcode}')
    def fill_new_customer(self, first_name: str, last_name: str, postcode: int) -> None:
        self.wait_for_element(self._FIRST_NAME)
        self.type(self._FIRST_NAME, first_name)
        self.type(self._LAST_NAME, last_name)
        self.type(self._POST_CODE, str(postcode))

    @allure.step('click add customer button')
    def click_add_customer(self) -> None:
        add_customer_button = self.wait_for_element(self._ADD_CUSTOMER_BUTTON)
        add_customer_button.click()

    @allure.step('get alert text')
    def get_alert_text(self) -> Union[str, None]:
        alert = self.driver.switch_to.alert
        return alert.text

    @allure.step('accept alert')
    def accept_alert(self) -> None:
        alert = self.driver.switch_to.alert
        alert.accept()
