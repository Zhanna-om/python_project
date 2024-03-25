from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest

browser=webdriver.Chrome()

def test_aut_positiv():
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url=="https://www.saucedemo.com/inventory.html"

def test_aut_negative():
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("user")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url=="https://www.saucedemo.com/"

def test_basket_add_product_1():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    #добавление в корзину через каталог
    time.sleep(3)
    browser.find_element(By.XPATH, '//div[contains(text(), "$")]/following-sibling::button').click()
    time.sleep(3)
    #переход в корзину и удаление
    browser.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    browser.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
    time.sleep(3)

def test_basket_add_product_2():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    #добавление в корзину через карточку
    browser.find_element(By.XPATH, '//div[contains(text(), "Backpack")]').click()
    browser.find_element(By.XPATH, '//button[contains(text(), "Add to cart")]').click()
    # удаление через карточку
    time.sleep(3)
    browser.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
    time.sleep(3)

def test_card_product():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    #клик по картинке
    browser.find_element(By.XPATH, '//img[@alt="Sauce Labs Bolt T-Shirt"]').click()
    assert browser.current_url=="https://www.saucedemo.com/inventory-item.html?id=1"

def test_product_card_name():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    #клик по названию
    browser.find_element(By.XPATH, '//div[contains(text(), "(Red)")]').click()
    assert browser.current_url=="https://www.saucedemo.com/inventory-item.html?id=3"

def test_placing_an_order():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    #добавление в корзину через каталог

    browser.find_element(By.XPATH, '//div[contains(text(), "$")]/following-sibling::button').click()

    #переход в корзину
    browser.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    browser.find_element(By.XPATH, '//button[contains(text(), "Checkout")]').click()
    #оформление товара
    browser.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Zhanna")
    browser.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Zhanna")
    browser.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("2")
    browser.find_element(By.XPATH, '//*[@id="continue"]').click()
    browser.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)
    browser.quit()

def test_filter_A_Z():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    browser.find_element(By.XPATH, '// select[ @class ="product_sort_container"]').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//button[contains(text(), "Z)")]').click()
    time.sleep(3)