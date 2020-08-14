from time import sleep
from selenium.webdriver import Firefox

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present


url = 'https://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()
wdw = WebDriverWait(browser, 30)

browser.get(url)

sleep(2)

browser.find_element_by_id('alertd').click()

print('before wait alert...')
alert = wdw.until(alert_is_present())
print('after wait alert.')

alert.accept()  # alerta
