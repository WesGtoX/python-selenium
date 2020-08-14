from time import sleep
from selenium.webdriver import Firefox


url = 'https://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()

browser.get(url)

sleep(2)

browser.find_element_by_id('alert').click()

alert = browser.switch_to.alert

alert.accept()   # Confirma, clica no OK
alert.dismiss()  # Confirma, clica no OK
