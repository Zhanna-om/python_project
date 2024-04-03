import time

from selenium.webdriver.common.by import By

from locator import *


def test_basket_add_product_1(authorise):
    browser = authorise
    # добавление в корзину через каталог
    browser.find_element(*add_to_card).click()
    # переход в корзину и удаление
    browser.find_element(*basket).click()
    browser.find_element(*remove).click()
    # проверка существует ли корзина
    try:
        browser.find_element(*quantity_of_goods)
    except:
        result = True
    assert result == True
    time.sleep(3)


def test_aut_negative(browser_init):
    browser = browser_init
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("user")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == "https://www.saucedemo.com/"
