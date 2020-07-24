from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.events import (
    AbstractEventListener, EventFiringWebDriver
)

from urllib.parse import urlparse
from time import sleep


class Listening(AbstractEventListener):

    def after_navigate_to(self, url, webdrive):
        print(f'Indo para ==> {url}')

    def after_navigate_back(self, webdriver):
        print('voltando para a página anterior')


def get_page(browser, url, tag='main'):
    browser.get(url)

    WebDriverWait(browser, 120).until(
        EC.presence_of_element_located((By.TAG_NAME, tag))
    )

    sleep(1)


def get_links(browser, element):  # dict
    """
    Pega todos os links dentro de um elemento

    - browser = a instancia do navegador
    - element = webelement [aside, main, body, ul, ol]
    """
    _element = browser.find_element_by_tag_name(element)
    anchors = _element.find_elements_by_tag_name('a')

    result = {}
    for anchor in anchors:
        result[anchor.text] = anchor.get_attribute('href')

    return result


def validate_answer(browser, key, answers, tag='main'):
    get_page(browser, url=answers[key], tag=tag)
    return browser.find_element_by_tag_name('main')


def verify_answer(page, tag='main'):
    for key in page.keys():
        text = 'Sou o Diabão do erro'
        if text in validate_answer(browser, key, page, tag).text:
            browser.back()
        else:
            break


browser = Firefox()

rapi_browser = EventFiringWebDriver(browser, Listening())

get_page(rapi_browser, url='https://selenium.dunossauro.live/aula_04.html')

classes = get_links(rapi_browser, 'aside')
exercises = get_links(rapi_browser, 'main')
get_page(rapi_browser, url=exercises['Exercício 3'])

start_here = get_links(rapi_browser, 'main')
get_page(rapi_browser, url=start_here['Começar por aqui'])

answers = get_links(rapi_browser, 'main')
verify_answer(page=answers, tag='li')

page_2 = get_links(rapi_browser, 'main')
verify_answer(page=page_2)

page_3 = get_links(rapi_browser, 'main')
end_url = urlparse(rapi_browser.current_url).path.split('/')[1]
check_page = validate_answer(rapi_browser, end_url, page_3)

if 'O diabão vai te pegar' in check_page.text:
    rapi_browser.refresh()
    sleep(1)

print(rapi_browser.find_element_by_tag_name('main').text)

rapi_browser.quit()
# Sou o unicórnio da salvação
#
#                \
#                 \\
#                  \%,     ,'     , ,.
#                   \%\,';/J,";";";;,,.
#      ~.------------\%;((`);)));`;;,.,-----------,~
#     ~~:           ,`;@)((;`,`((;(;;);;,`         :~~
#    ~~ :           ;`(@```))`~ ``; );(;));;,      : ~~
#   ~~  :            `X `(( `),    (;;);;;;`       :  ~~
#  ~~~~ :            / `) `` /;~   `;;;;;;;);,     :  ~~~~
# ~~~~  :           / , ` ,/` /     (`;;(;;;;,     : ~~~~
#   ~~~ :          (o  /]_/` /     ,);;;`;;;;;`,,  : ~~~
#    ~~ :           `~` `~`  `      ``;,  ``;" ';, : ~~
#     ~~:                             `'   `'  `'  :~~
#      ~`-----------------------------------------`~
#
# E você ganhou esse jogo
