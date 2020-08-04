from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    url_changes
)


url = 'https://selenium.dunossauro.live/aula_10_c.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 10)

link = browser.find_element_by_css_selector('.body_b a')
link.click()

wdw.until(
    url_changes(url),
)

print(url)
print(browser.current_url)

# https://selenium.dunossauro.live/aula_10_c.html#
# https://selenium.dunossauro.live/
# https://selenium.dunossauro.live/diabao.html
# https://selenium.dunossauro.live/unicornio.html
