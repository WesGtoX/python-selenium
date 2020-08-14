from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert


url = 'https://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()

browser.get(url)

sleep(2)

alert = Alert(browser)
# alert = browser.switch_to.alert  # NoAlertPresentException

browser.find_element_by_id('all').click()


alert.accept()  # alerta
sleep(1)
alert.send_keys('Wesley')  # prompt
sleep(1)
alert.accept()  # prompt
sleep(1)
alert.accept()  # confirm
