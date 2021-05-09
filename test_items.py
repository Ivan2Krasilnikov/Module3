import time


def test_shopcart_button_is_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(2)
    time.sleep(10)
    assert len(browser.find_elements_by_class_name("btn-primary")) > 0, "Кнопка 'Добавить в корзину' не найдена"
