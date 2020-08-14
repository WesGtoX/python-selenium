from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    alert_is_present,
    element_to_be_clickable,
)


url = 'https://selenium.dunossauro.live/exercicio_12.html'

browser = Firefox()
wdw = WebDriverWait(browser, 60)

browser.get(url)


def forms_propt(key: str, value: str):
    browser.find_element_by_css_selector(f'input[name="{key}"]').click()
    alert = wdw.until(alert_is_present())
    alert.send_keys(value)
    alert.accept()


def find_window(content: str):
    wids = browser.window_handles
    for window in wids:
        browser.switch_to.window(window)
        if content in browser.current_url:
            break


wdw.until(
    element_to_be_clickable(
        ('name', 'nome')
    )
)

input_list = {
    'nome': 'Wesley',
    'email': 'wesley@wesleymendes.com.br',
    'signo': 'Touro'
}

for k, v in input_list.items():
    forms_propt(k, v)

browser.find_element_by_css_selector('input.btn').click()

find_window('popup')

elements = browser.find_elements_by_tag_name('h1')

assert input_list.get('nome') in elements[1].text
assert input_list.get('email') in elements[2].text
assert input_list.get('signo') in elements[3].text
