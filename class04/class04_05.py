"""
1. Pegar todos os links de aulas.
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3.
    achar a url do exercício 3 e ir até lá.e
"""
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint


browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04.html')


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


"""
Parte 1
"""
sleep(1)

classes = get_links(browser, 'aside')

pprint(classes)

"""
browser.get(result['Aula 3'])
browser.get(result['Aula 4'])
"""

"""
Parte 2
"""

exercises = get_links(browser, 'main')
pprint(exercises)

browser.get(exercises['Exercício 3'])
