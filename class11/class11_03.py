from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert


url = 'https://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()

browser.get(url)

sleep(2)

browser.find_element_by_id('prompt').click()

alert = Alert(browser)

alert.send_keys('Wesley')

sleep(1)

alert.accept()   # Confirma, clica no OK
