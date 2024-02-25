import allure

from selenium.webdriver.remote.webdriver import WebDriver

from pages.addCust_page import AddCustPage
from pages.list_page import ListPage
from pages.base_page import BasePage


class Application:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.add_cust_page = AddCustPage(self)
        self.list_page = ListPage(self)
        self.base_page = BasePage(self)

    def construct_url(self, path: str = '') -> str:
        return self.base_url + path

    @allure.step("Open add customer page")
    def open_add_customer_page(self) -> AddCustPage:
        self.driver.get(self.construct_url("/addCust"))
        return self.add_cust_page

    @allure.step("Open customers page")
    def open_customers_page(self) -> ListPage:
        self.driver.get(self.construct_url("/list"))
        return self.list_page

    @allure.step("Open base page")
    def open_base_page(self) -> BasePage:
        self.driver.get(self.base_url)
        return self.base_page

