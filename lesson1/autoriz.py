from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import  Select
import pytest

browser=webdriver.Chrome()
def Authorization():
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    return browser.current_url=="https://www.saucedemo.com/inventory.html"