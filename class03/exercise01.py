# Exercício 01
# Crie um programa com selenium que
# - Gere um dicionário, onde a chave é a tag h1
#   - O valor deve ser um novo dicionário
#   - cada chave do valor deverá ser o valor de 'atributo'
#   - cada valor deve ser o texto contido no elemento
# Exemplo: {'H1': {'texto1': 'text','texto2': 'text','texto3': 'text'}}
# url: https://curso-python-selenium.netlify.app/exercicio_01.html

from selenium.webdriver import Firefox
from time import sleep


url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()
browser.get(url)

sleep(1)

key = browser.find_element_by_tag_name('h1')
values = browser.find_elements_by_tag_name('p')

key_tag = {key.text: {}}
for value in values:
    key_tag[key.text].update({value.get_attribute('atributo'): value.text})

print(key_tag)
# {'Boas vindas': {'texto1': 'Essa página é top de mais', 'texto2': 'E eu vou pegar todos os dados com selenium', 'texto3': 'Pq aqui não é brincadeira'}}

browser.quit()
