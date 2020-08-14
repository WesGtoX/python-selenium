from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert


url = 'https://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()

browser.get(url)

sleep(2)

alert = Alert(browser)

browser.find_element_by_id('confirm').click()

sleep(1)

alert.accept()   # Confirma, clica no OK
