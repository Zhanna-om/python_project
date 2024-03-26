from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import  Select
import pytest

browser=webdriver.Chrome()

def test_aut_positiv():
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    #time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    #time.sleep(1)
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
    #time.sleep(3)
    browser.find_element(By.XPATH, '//div[contains(text(), "$")]/following-sibling::button').click()
    #time.sleep(3)
    #переход в корзину и удаление
    browser.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    browser.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
    #time.sleep(3)

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
    #time.sleep(3)
    browser.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
    #time.sleep(3)

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
    #time.sleep(3)


def test_filter_Z_A():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    Select(browser.find_element(By.XPATH, '// select[ @class ="product_sort_container"]')).select_by_value("za")
    n=0
    for i in range(1,6):
        print(i)
        first_element=browser.find_element(By.XPATH, f'(//div[@class="inventory_item_name "])[{i}]').text
        next_element=browser.find_element(By.XPATH, f'(//div[@class="inventory_item_name "])[{i+1}]').text
        if first_element[0]<next_element[0]:
            n=n+1
        #print(first_element[0],next_element[0])
    #print(n)
    assert n==0

def test_filter_A_Z():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    Select(browser.find_element(By.XPATH, '// select[ @class ="product_sort_container"]')).select_by_value("az")
    n=0
    for i in range(1,6):
        #print(i)
        first_element=browser.find_element(By.XPATH, f'(//div[@class="inventory_item_name "])[{i}]').text
        next_element=browser.find_element(By.XPATH, f'(//div[@class="inventory_item_name "])[{i+1}]').text
        if first_element[0]>next_element[0]:
            n=n+1
        #print(first_element[0],next_element[0])
    #print(n)
    assert n==0



def test_filter_low_to_high():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    Select(browser.find_element(By.XPATH, '// select[ @class ="product_sort_container"]')).select_by_value("lohi")
    # n=0
    # for i in range(1,6):
    #     print(i)
    #     first_element=browser.find_element(By.XPATH, f'(//div[@class="inventory_item_price"])[{i}]').text
    #     next_element=browser.find_element(By.XPATH, f'(//div[@class="inventory_item_price"])[{i+1}]').text
    #     print(first_element, next_element)
    #     if first_element<=next_element:
    #         # print(first_element, next_element)
    #         # print("да")
    #         n=n+1
    #
    # print(n)
    # assert n==0

def test_filter_high_to_low():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    Select(browser.find_element(By.XPATH, '// select[ @class ="product_sort_container"]')).select_by_value("hilo")
    #time.sleep(3)



def test_open_menu_logout():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    #переход в бургер меню
    browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click()
    time.sleep(1)
    assert browser.current_url== "https://www.saucedemo.com/"
def test_about():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    #переход в бургер меню
    browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//a[@id="about_sidebar_link"]').click()
    time.sleep(1)
    assert browser.current_url== "https://saucelabs.com/"

    id = "reset_sidebar_link"

def test_reset_app_state():
    #авторизация
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    #переход в бургер меню
    browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//a[@id = "reset_sidebar_link"]').click()

    time.sleep(1)
