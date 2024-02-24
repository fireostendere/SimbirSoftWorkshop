import allure

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple, Union

faker = Faker()


class AddCustPage:
    """
    This class represents the Add Customer Page and contains methods to interact with it.
    """

    # Locators
    _FIRST_NAME: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(1) > .form-control')
    _LAST_NAME: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(2) > .form-control')
    _POST_CODE: Tuple[str, str] = (By.CSS_SELECTOR, '.form-group:nth-child(3) > .form-control')
    _ADD_CUSTOMER_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, '.btn-default')

    def __init__(self, app) -> None:
        self.driver: WebDriver = app.driver

    def type(self, locator: Tuple[str, str], value: str) -> 'AddCustPage':
        """
        This method types the given value into the field identified by the locator.
        """
        field = self.driver.find_element(*locator)
        current_value_in_field = field.get_attribute('value')
        if current_value_in_field != value:
            field.click()
            if current_value_in_field != '':
                field.clear()
            field.send_keys(value)
        return self

    @allure.step('generate random last name')
    def get_random_last_name(self) -> str:
        last_name = faker.last_name()
        allure.attach(last_name, name="Random Last Name", attachment_type=allure.attachment_type.TEXT)
        return last_name

    @allure.step('generate random postcode')
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

    @allure.step('fill customer form')
    def fill_new_customer(self) -> Tuple[str, str, int]:
        last_name = self.get_random_last_name()
        postcode = self.get_random_postcode()
        first_name = self.convert_postcode_to_name(postcode)
        self.type(self._FIRST_NAME, first_name)
        self.type(self._LAST_NAME, last_name)
        self.type(self._POST_CODE, str(postcode))
        return first_name, last_name, postcode

    @allure.step('click add customer button')
    def click_add_customer(self) -> None:
        self.driver.find_element(*self._ADD_CUSTOMER_BUTTON).click()

    @allure.step('check alert')
    def check_alert(self) -> bool:
        try:
            _ = self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    @allure.step('check alert text')
    def check_alert_text(self) -> Union[str, None]:
        if self.check_alert():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        return None
