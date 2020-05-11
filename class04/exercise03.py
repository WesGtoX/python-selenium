from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from time import sleep


def get_page(url, tag='main'):
    browser.get(url)

    WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.TAG_NAME, tag)))

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
    get_page(url=answers[key], tag=tag)
    return browser.find_element_by_tag_name('main')
    

def verify_answer(page, tag='main'):
    for key in page.keys():
        if 'Sou o Diabão do erro' in validate_answer(browser, key, page, tag).text:
            browser.back()
        else:
            break


browser = Firefox()
get_page(url='https://selenium.dunossauro.live/aula_04.html')

classes = get_links(browser, 'aside')
exercises = get_links(browser, 'main')
get_page(url=exercises['Exercício 3'])

start_here = get_links(browser, 'main')
get_page(url=start_here['Começar por aqui'])

answers = get_links(browser, 'main')
verify_answer(page=answers, tag='li')

page_2 = get_links(browser, 'main')
verify_answer(page=page_2)

page_3 = get_links(browser, 'main')
end_url = urlparse(browser.current_url).path.split('/')[1]
check_page = validate_answer(browser, end_url, page_3)

if 'O diabão vai te pegar' in check_page.text:
    browser.refresh()
    sleep(1)

print(browser.find_element_by_tag_name('main').text)

browser.quit()
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