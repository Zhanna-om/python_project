from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from locator import *


def test_aut_positiv(authorise):
    browser = authorise
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    assert browser.find_element(*title).text == "Products"  # проверяет наличие слова "Products" на странице
    assert len(browser.find_elements(*all_product)) == 6


def test_aut_negative(browser_init):
    browser = browser_init
    browser.get("https://www.saucedemo.com/")
    browser.find_element(*user_name).send_keys("user")
    browser.find_element(*password).send_keys("user")
    browser.find_element(*login).click()
    assert browser.current_url == "https://www.saucedemo.com/"


def test_basket_add_product_1(authorise):
    browser = authorise
    # авторизация
    # добавление в корзину через каталог
    browser.find_element(*add_to_card).click()
    # переход в корзину и удаление
    browser.find_element(*basket).click()
    browser.find_element(*remove).click()
    # проверка есть ли товар в корзине
    try:
        browser.find_element(*quantity_of_goods)
    except:
        result = True
    assert result == True
    assert browser.current_url == "https://www.saucedemo.com/cart.html"


def test_basket_add_product_2(authorise):
    browser = authorise
    # авторизация
    # добавление в корзину через карточку
    browser.find_element(*product_name).click()
    browser.find_element(*add_to_card).click()
    # удаление через карточку
    browser.find_element(*remove).click()
    # проверка есть ли товар в корзине
    try:
        browser.find_element(*quantity_of_goods)
    except:
        result = True
    assert result == True
    assert browser.current_url == "https://www.saucedemo.com/inventory-item.html?id=1"


def test_card_product(authorise):
    browser = authorise
    # авторизация
    # клик по картинке
    browser.find_element(*product_picture).click()
    assert browser.current_url == "https://www.saucedemo.com/inventory-item.html?id=1"  # переходит на нужную страницу
    assert browser.find_element(*add_to_cart_page_product).text == 'Add to cart'  # наличие кнопки на странице


def test_product_card_name(authorise):
    browser = authorise
    # авторизация
    # клик по названию
    browser.find_element(*product_name).click()
    assert browser.current_url == "https://www.saucedemo.com/inventory-item.html?id=1"  # переходит на нужную страницу
    assert browser.find_element(*add_to_cart_page_product).text == 'Add to cart'  # наличие кнопки на странице


def test_placing_an_order(authorise):
    browser = authorise
    # авторизация
    # добавление в корзину через каталог
    browser.find_element(*add_to_card).click()
    # переход в корзину
    browser.find_element(*basket).click()
    browser.find_element(*checkout).click()
    # оформление товара
    browser.find_element(*first_name).send_keys("Zhanna")
    browser.find_element(*last_name).send_keys("Zhanna")
    browser.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("2")
    browser.find_element(*button_continue).click()
    browser.find_element(*button_finish).click()


def test_filter_Z_A(authorise):
    browser = authorise
    # авторизация
    Select(browser.find_element(*button_filter)).select_by_value("za")
    product = browser.find_elements(*names_product)  # кортеж из названий всех продуктов уже отсортированных
    list = []
    for i in product:
        list.append(i.text)  # вытаскиваю текст из создаю картеж
    assert list == sorted(list, reverse=True)  # сравниваю полученый котреж c отсортированным
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    assert len(browser.find_elements(*all_product)) == 6


def test_filter_A_Z(authorise):
    browser = authorise
    # авторизация
    Select(browser.find_element(*button_filter)).select_by_value("az")
    product = browser.find_elements(*names_product)  # кортеж из названий всех продуктов уже отсортированных
    list = []
    for i in product:
        list.append(i.text)  # вытаскиваю текст из создаю картеж
    assert list == sorted(list)  # сравниваю полученый котреж c отсортированным
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    assert len(browser.find_elements(*all_product)) == 6


def test_filter_low_to_high(authorise):
    browser = authorise
    # авторизация
    Select(browser.find_element(By.XPATH, '// select[ @class ="product_sort_container"]')).select_by_value("lohi")
    price = browser.find_elements(*price_product)
    list = []
    for i in price:
        list.append(float(i.text[1:]))  # вытаскиваю цену без знака "$" из создаю картеж
    assert list == sorted(list)  # сравниваю полученый котреж c отсортированным
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    assert len(browser.find_elements(*all_product)) == 6


def test_filter_high_to_low(authorise):
    browser = authorise
    # авторизация
    Select(browser.find_element(By.XPATH, '// select[ @class ="product_sort_container"]')).select_by_value("hilo")
    price = browser.find_elements(*price_product)
    list = []
    for i in price:
        list.append(float(i.text[1:]))  # вытаскиваю цену без знака "$" из создаю картеж
    assert list == sorted(list, reverse=True)  # сравниваю полученый котреж c отсортированным
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    assert len(browser.find_elements(*all_product)) == 6


def test_open_menu_logout(authorise):
    browser = authorise
    # авторизация
    # переход в бургер меню
    browser.find_element(*menu).click()
    browser.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click()
    assert browser.current_url == "https://www.saucedemo.com/"


def test_about(authorise):
    browser = authorise
    # авторизация
    # переход в бургер меню
    browser.find_element(*menu).click()
    browser.find_element(By.XPATH, '//a[@id="about_sidebar_link"]').click()
    assert browser.current_url == "https://saucelabs.com/"
    id = "reset_sidebar_link"


def test_reset_app_state(authorise):
    browser = authorise
    # авторизация
    # переход в бургер меню
    browser.find_element(*menu).click()
    browser.find_element(By.XPATH, '//a[@id = "reset_sidebar_link"]').click()
    # проверка пуста ли корзина
    try:
        browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    except:
        result = True
    assert result == True
