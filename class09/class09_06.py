from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class WaitElementNotClick:

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        elements = webdriver.find_elements(*self.locator)
        if elements:
            return 'unclick' in elements[0].get_attribute('class')
        return False


def wait_element(by, element, webdriver):
    if webdriver.find_elements(by, element):
        return True
    return False


locator = (By.CSS_SELECTOR, 'button')
wait_button = WaitElementNotClick(locator)

url = 'https://selenium.dunossauro.live/aula_09.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until_not(wait_button, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(
    partial(wait_element, 'id', 'finished'),
    'A mensagem de sucesso não apareceu'
)

success = driver.find_element_by_css_selector('#finished')
assert success.text == 'Carregamento concluído'
