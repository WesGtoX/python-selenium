# Aula 17 - Selene

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2317.pdf)

## Sobre o Selene

- [Documentação]()
- [GitHub](https://github.com/yashaka/selene/)

O selene é baseado no Selenide, um wrapper do selenium feito do mundo java. Que não só automatiza tarefas, mas é um framework completo para testes.

Diferente do que vimos até agora com selenium original e o splinter. O Selene se propõem a resolver tanto as assertivas, quando a manipulação do browser e gerenciamento do webdriver.

## Instalação

```bash
pip install selene
pip install selene --pre  # (recommendedreco)
```

## Browser/WebDriver

### Manipulando o webdriver

A API do Selene é incrível e não manipula somente o browser. Mas se preocupa com a instalação do webdriver também.

### Webdriver config

#### browser.config

No selene as configurações são compartilhadas e simples de serem feitas usando um objeto único.

```python
from selene.support.shared import browser

url = 'http://selenium.dunossauro.live'

browser.config.browser_name = 'chrome'
browser.config.base_url = 'url'

browser.open('/caixinha')
```

### Driver Core API

#### Maneira "tradicional"

Quando for preciso especificar um browser não local, também podemos usar as formas tradicionais do selenium python. E ainda obter vantagens das configurações globais.

```python
from selene import Browser, Config
from selenium.webdriver import Firefox

browser = Browser(
    Config(
        driver=Firefox(),
        base_url='https://google.com'
    )
)
```


## Navegação

### Notas sobre a próxima parte

O selene ainda não tem uma API completa do selenium.

Nesse caso não temos como ir para frente e para trás usando o wrapper.

```python
browser.open(‘http://fsf.org’)
browser.driver.back()
browser.driver.forward()
```

### Navegando com Selene

- get() -> open()
- back() -> driver.back()
- forward() -> driver.forward()
- current_url -> driver.current_url
- title -> driver.title
- page_source -> driver.page_source

### Recursos legais de navegação

Embora os recursos primordiais estejam no driver e não no wrapper. Ainda podemos acessar a config.base_url que nos dá diversos confortos para trabalhar com várias páginas.

```python
browser.open('')           # Vai para a home
browser.open('/caixinha')  # Vai para caixinha
browser.open('/keyboard')  # Vai para teclado
```


## Interagindo com elementos

### Buscando elementos

Para buscar elementos com selene podemos os encontrar usando 3 formas diferentes:

- Driver
- jQuery style
- Conectivos By

A forma mais simples, é usar o próprio wrapper. Ele nos permite usar css e xpath.

```python
browser.element('[name="q"]')
browser.element('//*[@name="q"]')
```

Podemos achar mais de um elemento usando o driver.

```python
browser.element('[name="q"]')
browser.all('[name="q"]')

browser.element('//*[@name="q"]')
browser.all('//*[@name="q"]')
```

### Buscando elementos - jQuery style

No estilo jquery podemos escrever expressões menores que também são compatíveis com css e xpath.

```python
browser.s('//*[@name="q"]')
browser.ss('[name="q"]')
```

### Ou usando o `by`

```python
from selene import by

browser.element('[name="q"]')
browser.element(by.css('[name="q"]'))

browser.element('//*[@name="q"]')
browser.element(by.xpath('//*[@name="q"]'))
```


### Procurando elementos

| Selenium                             | Splinter        | Selene                 |
| ------------------------------------ | --------------- | ---------------------- |
| find_element_by_id()                 | find_by_id()    | by.id()                |
| find_elements_by_css_selector()      | find_by_css()   | by(), by.css()         |
| find_elements_by_tag_name()          | find_by_tag()   | ...                    |
| find_elements_by_xpath()             | find_by_xpath() | by(), by.xpath()       |
| find_elements_by_link_text()         | ...             | by.link_text()         |
| find_elements_by_partial_link_text() | ...             | by_partial_link_text() |
| find_elements_by_name()              | find_by_name()  | by.name()              |
| ...                                  | find_by_text()  | by.text()              |
| ...                                  | ...             | by.partial_text()      |
| ...                                  | find_by_value() | ...                    |


## Validadores

Temos alguns validadores incríveis no selene

- be
- have
- not


### As chamadas

Antes disso, precisamos aprender a chamar os validadores

```python
browser.open('/aula_07')

browser.s(by.name('nome')).click()

browser.s('[for="nome"]')..should(
    have.text('Não')
)
```

| be           | Descrição                                                   |
| ------------ | ----------------------------------------------------------- |
| be.visible   | Verifica se elemento está visível                           |
| be.hidden    | Verifica se elemento está oculto                            |
| be.selected  | Verifica se elemento está selecionado                       |
| be.present   | Verifica se elemento está presente (be.in_dom, be.existing) |
| be.absent    | Verifica se elemento está não está presente                 |
| be.enabled   | Verifica se elemento está habilitado                        |
| be.disabled  | Verifica se elemento está desabilitado                      |
| be.clickable | Verifica se elemento está é clicável (botões)               |
| be.blank     | Verifica se elemento está em branco (inputs)                |


| not           | Descrição                                                       |
| ------------- | --------------------------------------------------------------- |
| not.visible   | Verifica se elemento não está visível                           |
| not.hidden    | Verifica se elemento não está oculto                            |
| not.selected  | Verifica se elemento não está selecionado                       |
| not.present   | Verifica se elemento não está presente (be.in_dom, be.existing) |
| not.absent    | Verifica se elemento não está não está presente                 |
| not.enabled   | Verifica se elemento não está habilitado                        |
| not.disabled  | Verifica se elemento não está desabilitado                      |
| not.clickable | Verifica se elemento não está é clicável (botões)               |
| not.blank     | Verifica se elemento não está em branco (inputs)                |


| be\/not    | Descrição                                                           |
| ---------- | ------------------------------------------------------------------- |
| .visible   | Verifica se elemento está, ou não visível                           |
| .hidden    | Verifica se elemento está, ou não oculto                            |
| .selected  | Verifica se elemento está, ou não selecionado                       |
| .present   | Verifica se elemento está, ou não presente (be.in_dom, be.existing) |
| .absent    | Verifica se elemento está, ou não não está presente                 |
| .enabled   | Verifica se elemento está, ou não habilitado                        |
| .disabled  | Verifica se elemento está, ou não desabilitado                      |
| .clickable | Verifica se elemento está, ou não é clicável (botões)               |
| .blank     | Verifica se elemento está, ou não em branco (inputs)                |


### have

Have, são condições especiais em que a validação vai além do selenium.

#### Propriedades do HTML / CSS

- have.css_property(foo).value(bar)
- have.attribute(foo).value(bar)
- value
- value_containing
- css_class
- tag
- tag_containing

#### Tamanhos

- size
- size_less_than
- size_less_than_or_equal
- size_greater_than
- size_greater_than_or_equal

#### Tabs

- tabs_number
- tabs_number_less_than
- tabs_number_less_than_or_equal
- tabs_number_greater_than
- tabs_number_greater_than_or_equal

#### Outras opções legais

- title
- title_containing
- url
- url_containing
- text
- texts


## Nem tudo são flores

Sim, tá longe de ser perfeito

- Não tem documentação
- API em mudança constante
- Faz duas funções
- Lazy*
