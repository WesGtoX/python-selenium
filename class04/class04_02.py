from selenium.webdriver import Firefox


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


def find_by_href(browser, link):
    """Encontrar o elemento 'a' com o link 'link'.

    Argumentos
        - browser = Instancia do browser [firefox, chrome, ...].
        - link = link que será procurado em todas as tags 'a'.
    """
    elements = browser.find_elements_by_tag_name('a')

    for element in elements:
        if link in element.get_attribute('href'):
            return element

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

# element_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
element_ddg = find_by_href(browser, 'ddg')
