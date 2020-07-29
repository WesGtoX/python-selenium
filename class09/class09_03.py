from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait


def wait_element(element, webdriver):
    print(f'Tentando encontrar "{element}"')
    if webdriver.find_elements_by_css_selector(element):
        return True
    return False


wait_button = partial(wait_element, 'button')
wait_success = partial(wait_element, '#finished')

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until(wait_button, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(wait_success, 'A mensagem de sucesso não apareceu')

success = driver.find_element_by_css_selector('#finished')
assert success.text == 'Carregamento concluído'
