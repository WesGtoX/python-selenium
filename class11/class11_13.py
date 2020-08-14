from time import sleep
from selenium.webdriver import Firefox


url = 'https://selenium.dunossauro.live/aula_11_d.html'

browser = Firefox()

browser.get(url)

sleep(2)

browser.switch_to.frame('iframe')

browser.find_element_by_id('nome').send_keys('Wesley')
browser.find_element_by_id('email').send_keys('wesley@wesleymendes.com.br')
browser.find_element_by_id('senha').send_keys('123456')
