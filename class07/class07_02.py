"""
1. Checar se a mudança ocorre no span (focus, blur) - OK
2. Checar se a mudança ocorre no p (change)
"""
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener, EventFiringWebDriver
)


class Listening(AbstractEventListener):

    def after_navigate_to(self, url, webdrive):
        print(f'Indo para {url}')

    def after_navigate_back(self, webdriver):
        print('voltando para a página anterior')

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'antes do click no {elemento.tag_name}')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'depois do click no {elemento.tag_name}')


browser = Firefox()

rapi_browser = EventFiringWebDriver(browser, Listening())

rapi_browser.get('https://selenium.dunossauro.live/aula_07_d')

text_input = rapi_browser.find_element_by_tag_name('input')
span = rapi_browser.find_element_by_tag_name('span')
p = rapi_browser.find_element_by_tag_name('p')

text_input.click()
span.click()

rapi_browser.get('https://selenium.dunossauro.live/aula_07_c')
rapi_browser.back()

browser.quit()
