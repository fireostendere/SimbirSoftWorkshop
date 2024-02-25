import allure

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple, Union

from pages.base_page import BasePage

faker = Faker()


class AddCustPage(BasePage):
    """
    This class represents the Add Customer Page and contains methods to interact with it.
    """

    # Locators
    _FIRST_NAME: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(1) > .form-control')
    _LAST_NAME: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(2) > .form-control')
    _POST_CODE: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(3) > .form-control')
    _ADD_CUSTOMER_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '.btn-default')

    def get_random_last_name(self) -> str:
        last_name = faker.last_name()
        allure.attach(last_name, name="Random Last Name", attachment_type=allure.attachment_type.TEXT)
        return last_name

    def get_random_postcode(self) -> int:
        postcode = faker.random_number(digits=10)
        allure.attach(str(postcode), name='Random Postcode', attachment_type=allure.attachment_type.TEXT)
        return postcode

    @allure.step('convert postcode to name')
    def convert_postcode_to_name(self, postcode: int) -> str:
        postcode_as_string = str(postcode)
        first_name = ''
        for i in range(0, len(postcode_as_string), 2):
            digit = int(postcode_as_string[i:i + 2])
            first_name += chr(97 + digit % 26)
        first_name = first_name.capitalize()
        allure.attach(first_name, name='First Name from Postcode', attachment_type=allure.attachment_type.TEXT)
        return first_name

    @allure.step('fill customer form with first name: {first_name}, last name: {last_name}, and postcode: {postcode}')
    def fill_new_customer(self, first_name: str = None, last_name: str = None, postcode: int = None) -> None:
        self.wait_for_element(self._FIRST_NAME)
        self.type(self._FIRST_NAME, first_name)
        self.type(self._LAST_NAME, last_name)
        self.type(self._POST_CODE, str(postcode))

    @allure.step('click add customer button')
    def click_add_customer(self) -> None:
        add_customer_button = self.wait_for_element(self._ADD_CUSTOMER_BUTTON)
        add_customer_button.click()

    @allure.step('is alert present')
    def is_alert_present(self) -> bool:
        return self.wait_for_alert()

    @allure.step('get alert text')
    def get_alert_text(self) -> Union[str, None]:
        alert = self.driver.switch_to.alert
        return alert.text

    @allure.step('accept alert')
    def accept_alert(self) -> None:
        alert = self.driver.switch_to.alert
        alert.accept()
