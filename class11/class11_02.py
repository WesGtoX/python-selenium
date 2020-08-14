from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert


url = 'https://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()

browser.get(url)

sleep(2)

browser.find_element_by_id('alert').click()

alert = Alert(browser)           # Lida com erros
alert = browser.switch_to.alert  # Não lida com erros

alert.accept()   # Confirma, clica no OK
alert.dismiss()  # Confirma, clica no OK
