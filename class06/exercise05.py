import getpass
from selenium.webdriver import Firefox
from time import sleep


def open_browser(browser, url):
    return browser.get(url)


def close_broser(browser):
    return browser.quit()


def fill_form(browser, form, nome, senha):
    browser.find_element_by_css_selector(
        f'.form-{form} input[name="nome"]').send_keys(nome)

    browser.find_element_by_css_selector(
        f'.form-{form} input[name="senha"]').send_keys(senha)

    sleep(1)

    browser.find_element_by_css_selector(
        f'.form-{form} input[name="{form}"]').click()


def get_header_text(browser):
    return browser.find_element_by_css_selector('p span').text


def form_iterate(browser, data, i=0):
    input_form = len(
        browser.find_elements_by_css_selector('form[class*="form-l"]')
    )

    for i in range(input_form):
        _form = browser.find_element_by_css_selector('p span').text
        fill_form(browser, _form, **data)
        i += 1
        sleep(1)


def get_it_done(browser, url, data):
    open_browser(browser, url)

    sleep(2)

    form_iterate(browser, data)

    done = "você conseguiu terminar"
    if done in get_header_text(browser):
        return f'\n{":"*32}\n:: {done.upper()}!!! ::\n{":"*32}\n'
    else:
        print('Houve algum problema, vamos tentar novamente!')


if __name__ == "__main__":
    browser = Firefox()
    url = 'https://selenium.dunossauro.live/exercicio_05.html'

    name = passwd = ''

    while len(name) < 1 > len(passwd):
        name = input('Digite o seu nome: ')
        passwd = getpass.getpass(prompt='Digite a sua senha: ')

    data = {
        'nome': name,
        'senha': passwd,
    }

    print(get_it_done(browser, url, data))
    close_broser(browser)
