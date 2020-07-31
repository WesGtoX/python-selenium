from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def wait_element(by, element, webdriver):
    if 'todo' in element:
        print(
            f'Tentando encontrar "{element}" by {by} para fazer a tarefa'
        )
    if 'doing' in element:
        print(
            f'Tentando encontrar "{element}" by {by} para finalizar a tarefa'
        )
    if 'done' in element:
        print(
            f'Tentando encontrar "{element}" by {by} para refazer a tarefa'
        )

    if webdriver.find_elements(by, element):
        if 'todo' in element:
            print('Fazendo a tarefa!')
        if 'doing' in element:
            print('Tarefa finalizada!')
        if 'done' in element:
            print('Se preparando para refazer a tarefa!')
        webdriver.find_element(by, element).click()
        return True
    return False


def wait_to(wdw, selector, error_message):
    wdw.until(
        partial(wait_element, By.CSS_SELECTOR, selector),
        error_message
    )


def create_task(d):
    d.find_element_by_css_selector(
        '#todo-name').send_keys('Curso de Selenium')
    d.find_element_by_css_selector(
        '#todo-desc').send_keys('Terminar o Curso de Selenium')
    d.find_element_by_css_selector(
        '#todo-submit').click()


url = 'https://selenium.dunossauro.live/exercicio_10.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

create_task(driver)

task_list = [
    {
        'selector': '#todo button.do',
        'error_message': 'Deu ruim ao começar a fazer a tarefa'
    },
    {
        'selector': '#doing button.do',
        'error_message': 'Deu ruim quando estava realizando a tarefa'
    },
    {
        'selector': '#done button.do',
        'error_message': 'Deu ruim ao terminar a tarefa'
    },
    {
        'selector': '#todo button.do',
        'error_message': 'Deu ruim ao tentar refazer a tarefa'
    }
]

for task in task_list:
    wait_to(wdw, **task)
