from selenium.webdriver import Firefox
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    _find_element, url_contains,
    text_to_be_present_in_element_value
)


def wait_filled_input():
    input_list = ['nome', 'email', 'c_email', 'senha', 'c_senha']
    input_text = {
        'nome': 'Fausto',
        'email': 'fausto@faustino.faust',
        'c_email': 'fausto@faustino.faust',
        'senha': '123456*',
        'c_senha': '123456*'
    }

    for name in input_list:
        locator = (By.CSS_SELECTOR, f'input[name="{name}"]')
        wdw.until(
            text_to_be_present_in_element_value(
                locator,
                'disponível'
            ),
        )
        print(f'Preencher {name}: {input_text[name]}')
        browser.find_element(*locator).send_keys(input_text[name])


class TextPresentInElementValue(object):

    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_
        self.filled = False

    def __call__(self, driver):
        if not self.filled:
            wait_filled_input()
        self.filled = True

        try:
            element_text = _find_element(
                driver, self.locator).get_attribute("value")
            if element_text:
                return self.text in element_text
            else:
                return False
        except StaleElementReferenceException:
            return False


url = 'https://selenium.dunossauro.live/exercicio_11.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 60)

locator = (By.CSS_SELECTOR, 'input.btn')
wdw.until(
    TextPresentInElementValue(locator, 'disponível'),
    'O botão não ficou disponível'
)

print('Enviar form...')
browser.find_element_by_css_selector('input.btn').click()

wdw.until(
    url_contains('?nome='),
)
print('Form enviado!')
