from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait


def wait_button(webdriver):
    elements = webdriver.find_elements_by_css_selector('button')
    print('Tentando encontrar "button"')
    return bool(elements)  # True ou False


def wait_success(webdriver):
    elements = webdriver.find_elements_by_css_selector('#finished')
    print('Tentando encontrar "finished"')
    return bool(elements)  # True ou False


url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until(wait_button, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(wait_success, 'A mensagem de sucesso não apareceu')

success = driver.find_element_by_css_selector('#finished')
assert success.text == 'Carregamento concluído'
