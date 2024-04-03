import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from locator import *


@pytest.fixture(scope="module")
def browser_init():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    return browser


@pytest.fixture
def authorise(browser_init):
    browser = browser_init
    browser.get("https://www.saucedemo.com/")
    browser.find_element(*user_name).send_keys("standard_user")
    # time.sleep(1)
    browser.find_element(*password).send_keys("secret_sauce")
    # time.sleep(1)
    browser.find_element(*login).click()
    return browser
