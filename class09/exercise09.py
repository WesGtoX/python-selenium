from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def wait_element(by, element, webdriver):
    print(f'Tentando encontrar "{element}" by {by}')
    if webdriver.find_elements(by, element):
        print(f'Esperei até encontrar a classe "{element}"!')
        return True
    return False


url = 'https://selenium.dunossauro.live/exercicio_09'

driver = Firefox()

wdw = WebDriverWait(driver, 30)

driver.get(url)

wdw.until(
    partial(wait_element, By.CLASS_NAME, 'selenium'),
    'A class selenium não apareceu...'
)
