from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    frame_to_be_available_and_switch_to_it,
    element_to_be_clickable
)


url = 'https://selenium.dunossauro.live/aula_11_d.html'

browser = Firefox()
wdw = WebDriverWait(browser, 60)

browser.get(url)

wdw.until(
    frame_to_be_available_and_switch_to_it(
        ('name', 'iframe')
    )
)

wdw.until(
    element_to_be_clickable(
        ('name', 'nome')
    )
)

browser.find_element_by_id('nome').send_keys('Wesley')
browser.find_element_by_id('email').send_keys('wesley@wesleymendes.com.br')
browser.find_element_by_id('senha').send_keys('123456')
