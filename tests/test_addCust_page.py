import re
import allure

from typing import Any


@allure.feature('addCust page')
@allure.story('Add customer')
@allure.title('Add customer and check alert message')
def test_add_customer(app: Any) -> None:
    allert_pattern = r'Customer added successfully with customer id :(\d+)'
    add_customer_page = app.open_add_customer_page()
    first_name = add_customer_page.get_random_last_name()
    postcode = add_customer_page.get_random_postcode()
    last_name = add_customer_page.convert_postcode_to_name(postcode)
    add_customer_page.fill_new_customer(first_name=first_name, last_name=last_name, postcode=postcode)
    add_customer_page.click_add_customer()
    assert add_customer_page.is_alert_present(), 'Alert is not present'
    alert_text = add_customer_page.get_alert_text()
    assert re.search(allert_pattern, alert_text), 'Incorrect alert text'
    add_customer_page.accept_alert()
