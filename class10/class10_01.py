from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_all_elements_located
)


url = 'https://selenium.dunossauro.live/aula_10_a.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 30)


locator = (By.CSS_SELECTOR, '#request')

wdw.until(
    presence_of_all_elements_located(locator)
)

browser.find_element(*locator).click()
