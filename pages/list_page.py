import allure

from selenium.webdriver.common.by import By
from typing import List

from pages.base_page import BasePage


class ListPage(BasePage):
    """
    This class represents the List Page and contains methods to interact with it.
    """

    # Locators
    _DELETE_BUTTONS = (By.CSS_SELECTOR, '.ng-scope td > button')
    _FIRST_NAME_BUTTON = (By.XPATH, "//a[contains(.,'First Name')]")
    _FIRST_NAME_FIELDS = (By.CSS_SELECTOR, '.ng-scope > .ng-binding:nth-child(1)')

    @allure.step('click sort button')
    def click_sort_button(self) -> None:
        """
        This method clicks the sort button on the page.
        """
        sort_button = self.wait_for_element(self._FIRST_NAME_BUTTON)
        sort_button.click()

    @allure.step('get first name list')
    def get_first_name_list(self) -> List[str]:
        """
        This method retrieves the list of first names from the page.
        """
        first_name_fields = self.wait_for_elements(self._FIRST_NAME_FIELDS)
        names = [field.text for field in first_name_fields]
        return names

    @allure.step('get closest to average name')
    def get_closest_to_average_name(self, names) -> str:
        """
        This method retrieves the name whose length is closest to the average name length.
        """
        lengths = [len(name) for name in names]
        average_length = sum(lengths) / len(lengths)
        closest_name = min(names, key=lambda name: abs(len(name) - average_length))
        return closest_name

    @allure.step('get index of name')
    def get_index_of_name(self, name: str) -> int:
        """
        This method retrieves the index of the given name in the list of names on the page.
        """
        names = self.get_first_name_list()
        index = names.index(name)
        return index

    @allure.step('click delete button')
    def click_delete_button(self, index: int) -> None:
        """
        This method clicks the delete button of the customer at the given index.
        """
        delete_buttons = self.driver.find_elements(*self._DELETE_BUTTONS)
        delete_buttons[index].click()
