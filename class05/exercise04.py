import json
from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse


url = 'https://selenium.dunossauro.live/exercicio_04.html'

firefox = Firefox()

firefox.get(url)

sleep(2)

def fill_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

struct = {
    'nome': 'Wesley', 
    'email': 'wesley@wesley.com', 
    'senha': 'q1w2e3r4', 
    'telefone': '991993862'
}

fill_form(firefox, **struct)

parser_url = urlparse(firefox.current_url)

sleep(2)

text_result = firefox.find_element_by_tag_name('textarea').text
text_result_fixed = text_result.replace('\'', '\"')

dict_result = json.loads(text_result_fixed)

assert dict_result == struct

firefox.quit()
