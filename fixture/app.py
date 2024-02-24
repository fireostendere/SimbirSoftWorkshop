from typing import Optional
import allure

from selenium.webdriver.remote.webdriver import WebDriver

from pages.addCust_page import AddCustPage
from pages.list_page import ListPage


class Application:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(2)
        self.base_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        self.add_cust_page: Optional[AddCustPage] = None
        self.list_page: Optional[ListPage] = None

    def construct_url(self, path: str = '') -> str:
        return self.base_url + path

    @allure.step("Open add customer page")
    def open_add_customer_page(self) -> AddCustPage:
        self.driver.get(self.construct_url("/addCust"))
        if not self.add_cust_page:
            self.add_cust_page = AddCustPage(self)
        return self.add_cust_page

    @allure.step("Open customers page")
    def open_customers_page(self) -> ListPage:
        self.driver.get(self.construct_url("/list"))
        if not self.list_page:
            self.list_page = ListPage(self)
        return self.list_page
