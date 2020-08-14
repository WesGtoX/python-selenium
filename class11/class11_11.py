from selenium.webdriver import Firefox

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    new_window_is_opened, number_of_windows_to_be
)


url = 'https://selenium.dunossauro.live/aula_11_b.html'

browser = Firefox()
wdw = WebDriverWait(browser, 60)

browser.get(url)

browser.execute_script('window.open("_blank")')

wdw.until(
    new_window_is_opened(browser.window_handles)
)

wdw.until(
    number_of_windows_to_be(4)
)

browser.switch_to.window(browser.window_handles[-1])

browser.get('https://ddg.gg')
