from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def wait_element(by, element, webdriver):
    print(f'Tentando encontrar "{element}" by {by}')
    if webdriver.find_elements(by, element):
        return True
    return False


wait_button = partial(wait_element, By.CSS_SELECTOR, 'button')
# wait_success = partial(wait_element, '#finished')

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until(wait_button, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(
    partial(wait_element, 'id', 'finished'),
    'A mensagem de sucesso não apareceu'
)

success = driver.find_element_by_css_selector('#finished')
assert success.text == 'Carregamento concluído'
