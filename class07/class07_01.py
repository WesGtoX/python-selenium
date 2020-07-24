"""
1. Checar se a mudança ocorre no span (focus, blur) - OK
2. Checar se a mudança ocorre no p (change)
"""
from selenium.webdriver import Firefox


url = 'https://selenium.dunossauro.live/aula_07_d'

browser = Firefox()

browser.get(url)

text_input = browser.find_element_by_tag_name('input')
span = browser.find_element_by_tag_name('span')
p = browser.find_element_by_tag_name('p')

"""
Quando clicar no elemento `input`
Então o texto 'está com foco' deve ser o content de `span`
Quando clicar no elemento `span`
Então o texto 'está sem foco' deve ser o content de `span`
"""
text_input.click()
assert 'está com foco' == span.text, 'está com foco não está em span'
span.click()
assert 'está sem foco' == span.text, 'está sem foco não está em span'

"""
Dado que o texto '0' deve ser o content de `p`
Quando enviar 'batata' no elemento `input`
Então o texto 'está com foco' deve ser o content de `span`
Quando clicar no elemento `span`
Então o texto 'está sem foco' deve ser o content de `span`
Então o texto '1' deve ser o content de `p`
"""
assert p.text == '0', 'p não é zero'
text_input.send_keys('batata')
assert 'está com foco' == span.text, 'está com foco não está em span'
span.click()
assert 'está sem foco' == span.text, 'está com foco não está em span'
assert p.text == '1', 'p não é um'


browser.quit()
