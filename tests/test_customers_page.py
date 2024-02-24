import allure

from typing import Any


@allure.feature('List page')
@allure.story('Sort customers')
@allure.title('Reverse sort/Straight sort by first name and check it')
def test_sorted_by_first_name(app: Any) -> None:
    customers_page = app.open_customers_page()
    customers_page.click_sort_button()
    list_of_customers = customers_page.get_first_name_list()
    assert list_of_customers == sorted(list_of_customers, reverse=True), 'List is not reverse sorted'
    customers_page.click_sort_button()
    list_of_customers = customers_page.get_first_name_list()
    assert list_of_customers == sorted(list_of_customers), 'List is not sorted'


@allure.feature('List page')
@allure.story('Delete customer')
@allure.title('Delete customer closest to average age and check it')
def test_delete_customer(app: Any) -> None:
    customers_page = app.open_customers_page()
    old_list_of_customers = customers_page.get_first_name_list()
    deleted_name = customers_page.delete_customer_closest_to_average()
    new_list_of_customers = customers_page.get_first_name_list()
    old_list_of_customers.remove(deleted_name)
    assert old_list_of_customers == new_list_of_customers, 'Customer was not deleted'
