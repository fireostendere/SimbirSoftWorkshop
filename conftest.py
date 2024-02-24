import allure
import pytest

from fixture.app import Application
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest


def pytest_addoption(parser: Parser) -> None:
    """
    Add command line option for selecting the browser.
    """
    parser.addoption("--browser", action="store", default="chrome")


def driver_factory(browser: str) -> WebDriver:
    """
    Create a WebDriver instance based on the browser choice.
    """
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    return driver


@pytest.fixture(scope="session")
def app(request: FixtureRequest) -> Application:
    """
    Create an Application instance with a WebDriver.
    This fixture has session scope, so the Application instance will be created once per test session.
    """
    browser = request.config.getoption("--browser")
    driver = driver_factory(browser)
    app = Application(driver=driver)

    yield app

    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        if "app" in item.funcargs:
            allure.attach(
                body=item.funcargs["app"].driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
