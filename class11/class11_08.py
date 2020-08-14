from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait


url = 'https://selenium.dunossauro.live/aula_11_b.html'


browser = Firefox()
wdw = WebDriverWait(browser, 30)

browser.get(url)

sleep(2)

browser.current_window_handle  # id da janela atual
wids = browser.window_handles  # id's de todas as janelas


def find_window(content: str):
    wids = browser.window_handles
    for window in wids:
        browser.switch_to.window(window)
        if content in browser.page_source.lower():
            break


browser.find_element_by_id('popup').click()

find_window('<h1>popup')

browser.page_source
