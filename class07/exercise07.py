"""
1. Preencher formulário
2. Qual a modificação do label
  - antes: 'nome' | 'email' | 'senha'
  - durante: 'Não vale mentir o nome' | 'Esse email é mesmo válido?' | 'Já falei pra não colocar 1234' # noqa
  - depois: 'nome' | 'email' | 'senha'
3. Mostrar resultado
"""
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener, EventFiringWebDriver
)


class Listening(AbstractEventListener):

    def before_click(self, element, webdriver):
        if element.tag_name == 'label':
            print(f'\nbefore ==> {element.text}')
            self._input_text(element.text, webdriver)

    def after_click(self, element, webdriver):
        if element.tag_name == 'label':
            print(f'during ==> {element.text}')
            webdriver.find_element_by_tag_name('body').click()
            print(f'after  ==> {element.text}')

    def _input_text(self, text, webdriver):
        if text == 'nome:':
            input_send = webdriver.find_element_by_tag_name('input#nome')
            input_send.send_keys('Wesley')

        if text == 'email:':
            webdriver.find_element_by_tag_name('input#email')
            input_send.send_keys('wesley@wesleymendes.com')

        if text == 'senha:':
            webdriver.find_element_by_tag_name('input#senha')
            input_send.send_keys('1234*')


browser = Firefox()

rapi_browser = EventFiringWebDriver(browser, Listening())

rapi_browser.get('https://selenium.dunossauro.live/exercicio_07')

sleep(2)

name_label = rapi_browser.find_element_by_tag_name('label#lnome')
name_label.click()

email_label = rapi_browser.find_element_by_tag_name('label#lemail')
email_label.click()

passwd_label = rapi_browser.find_element_by_tag_name('label#lsenha')
passwd_label.click()

browser.find_element_by_tag_name('input#btn').click()
