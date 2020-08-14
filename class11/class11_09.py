from time import sleep
from selenium.webdriver import Firefox

from selenium.webdriver.support.wait import WebDriverWait


url = 'https://selenium.dunossauro.live/aula_11_c.html'


browser = Firefox()
wdw = WebDriverWait(browser, 30)

browser.get(url)

sleep(2)

print(f'Janelas: {len(browser.window_handles)}')
browser.find_element_by_tag_name('button').click()
print(f'Janelas: {len(browser.window_handles)}')
