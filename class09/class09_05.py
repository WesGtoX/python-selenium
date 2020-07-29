from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class WaitElement:

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False


locator = (By.CSS_SELECTOR, 'button')
wait_button = WaitElement(locator)

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until(wait_button, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(
    WaitElement(locator=('id', 'finished')),
    'A mensagem de sucesso não apareceu'
)

success = driver.find_element_by_css_selector('#finished')
assert success.text == 'Carregamento concluído'
