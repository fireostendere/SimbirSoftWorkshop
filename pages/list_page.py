import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class ListPage:
    """
    This class represents the List Page and contains methods to interact with it.
    """

    # Locators
    _DELETE_BUTTONS = (By.CSS_SELECTOR, '.ng-scope td > button')
    _FIRST_NAME_BUTTON = (By.XPATH, "//a[contains(.,'First Name')]")
    _FIRST_NAME_FIELDS = (By.CSS_SELECTOR, '.ng-scope > .ng-binding:nth-child(1)')

    def __init__(self, app):
        self.driver: WebDriver = app.driver

    @allure.step('click sort button')
    def click_sort_button(self) -> None:
        """
        This method clicks the sort button on the page.
        """
        self.driver.find_element(*self._FIRST_NAME_BUTTON).click()

    @allure.step('get first name list')
    def get_first_name_list(self) -> List[str]:
        """
        This method retrieves the list of first names from the page.
        """
        first_name_fields = self.driver.find_elements(*self._FIRST_NAME_FIELDS)
        names = [field.text for field in first_name_fields]
        return names

    @allure.step('delete customer closest to average')
    def delete_customer_closest_to_average(self) -> str:
        """
        This method deletes the customer whose name length is closest to the average name length.
        """
        names = self.get_first_name_list()
        lengths = [len(name) for name in names]
        average_length = sum(lengths) / len(lengths)
        closest_name = min(names, key=lambda name: abs(len(name) - average_length))
        index = names.index(closest_name)
        delete_buttons = self.driver.find_elements(*self._DELETE_BUTTONS)
        delete_buttons[index].click()
        return closest_name
