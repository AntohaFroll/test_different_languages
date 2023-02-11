import time
from selenium.webdriver.common.by import By


def test_find_button_add_to_basket(browser):
    browser.implicitly_wait(5)
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(5)
    button_add_to_basket = browser.find_element(By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    assert button_add_to_basket is not None, "Button 'Add to basket' not found!"
