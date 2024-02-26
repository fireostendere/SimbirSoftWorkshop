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
        self.presence_element(self._FIRST_NAME_BUTTON).click()

    @allure.step('get first name list')
    def get_first_name_list(self) -> List[str]:
        """
        This method retrieves the list of first names from the page.
        """
        first_name_fields = self.wait_for_elements(self._FIRST_NAME_FIELDS)
        names = [field.text for field in first_name_fields]
        return names

    @allure.step('click delete button')
    def click_delete_button(self, index: int) -> None:
        """
        This method clicks the delete button of the customer at the given index.
        """
        delete_buttons = self.driver.find_elements(*self._DELETE_BUTTONS)
        delete_buttons[index].click()
