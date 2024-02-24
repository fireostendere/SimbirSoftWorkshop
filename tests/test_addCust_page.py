import re
import allure

from typing import Any


@allure.feature('addCust page')
@allure.story('Add customer')
@allure.title('Add customer and check alert message')
def test_add_customer(app: Any) -> None:
    aller_pattern = r'Customer added successfully with customer id :(\d+)'
    add_customer_page = app.open_add_customer_page()
    add_customer_page.fill_new_customer()
    add_customer_page.click_add_customer()
    assert add_customer_page.check_alert(), 'Alert is not present'
    alert_text = add_customer_page.check_alert_text()
    assert re.search(aller_pattern, alert_text), 'Incorrect alert text'
