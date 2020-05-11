from selenium.webdriver import Firefox
from time import sleep


def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto 'text'.

    Argumentos
        - browser = Instancia do browser [firefox, chrome, ...].
        - text = conteúdo que deve estar na tag.
        - tag = tag onde o texto será procurado.
    """
    elements = browser.find_elements_by_tag_name(tag)  # list

    for element in elements:
        if element.text == text:
            return element

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

# 'https://selenium.dunossauro.live/selected=box-1'

box_name = ['um', 'dois', 'tres', 'quatro']

for text in box_name:
    find_by_text(browser, 'div', text).click()

for text in box_name:
    sleep(0.3)
    browser.back()

for text in box_name:
    sleep(0.3)
    browser.forward()
