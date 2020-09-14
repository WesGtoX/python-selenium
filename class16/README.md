# Aula 16 - Splinter

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2316.pdf)

## Sobre o Splinter

- [Documentação](https://splinter.readthedocs.io/en/latest/)
- [GitHub](https://github.com/cobrateam/splinter)


## Instalação

```bash
pip install splinter
```

## Browser/WebDriver

### Manipulando o webdriver

O splinter fornece uma API **muito simples** para manipular o browser e facilita as chamadas de import.

```python
from splinter import Browser

b = Browser()
b = Browser(headless=True)
b = Browser(incognito=True)
```

Para alternar entre os browsers não é necessário mudar a forma dos imports, o que facilita um bocado.

```python
from splinter import Browser

b = Browser('firefox)
b = Browser('chrome)
```

Webdrivers remotos respeitam a mesma API.

```python
from splinter import Browser

b = Browser(
    driver_name='remote',
    browser='firefox',
    command_executor='http:/127.0.0.1:4444/wd/hub',
    desired_capabilities={'plataform': 'LINUX'}
)
```

### Possíveis problemas

Caso você tenha problemas com a importação e o uso de paths para os executáveis.

```python
from splinter import Browser

executable_path = {'executable_path': '</path/to/chrome>'}
browser = Browser('chrome', **executable_path)
```


## Navegação

```python
browser.visit(‘http://fsf.org’)
browser.back()
browser.forward()
```

### Navegando com Splinter

- get() -> visit()
- back()
- forward()
- current_url -> url
- title
- page_source -> html


## Interagindo com elementos

O splinter nos permite fazer as mesmas buscas e interações que o selenium nos permite, porém com uma API mais simplificada. Por exemplo, procurar "live de python" no google.

```python
from splinter import Browser

b = Browser()
b.visit('http://google.com')
b.find_by_css('[name="q"]').type('Live de Python')
b.find_by_name('btnkK').click()
```

#### Como estamos fazendo?

```python
from splinter import Browser

b = Browser()

b.visit('http://selenium.dunossauro.live/aula_07.html')

b.find_by_id('nome').type('Fautinho')
b.find_by_id('email').type('faut@o.com')
b.find_by_id('senha').type('1234')
```


#### Fill e Type

Type usa a low level API do selenium. Onde faz keyUp e keyDown. Tem lugares onde precisamos usar type.

Porém, em formulários, é necessário que o input tenha um nome (name) e nesse caso a opção fill pode nos ajudar.

```python
b.fill('name', 'text')
```

### Encontrar

#### Procurando elementos

| Selenium                             | Splinter        |
| ------------------------------------ | --------------- |
| find_element_by_id()                 | find_by_id()    |
| find_elements_by_css_selector()      | find_by_css()   |
| find_elements_by_tag_name()          | find_by_tag()   |
| find_elements_by_xpath()             | find_by_xpath() |
| find_elements_by_class_name()        | ...             |
| find_elements_by_link_text()         | ...             |
| find_elements_by_partial_link_text() | ...             |
| find_elements_by_name()              | find_by_name()  |
| ...                                  | find_by_text()  |
| ...                                  | find_by_value() |

#### Procurando links

| Selenium                             | Splinter        |
| ------------------------------------ | --------------- |
| find_elements_by_link_text()         | ...             |
| find_elements_by_partial_link_text() | ...             |

```python
b.links.find_by_text()
b.links.find_by_partial_text()
b.links.find_by_href()
b.links.find_by_partial_href()

b.find_by_css('selector').find_by_text()
b.find_by_css('selector').find_by_partial_text()
b.find_by_css('selector').find_by_href()
b.find_by_css('selector').find_by_partial_href()
```

#### Lazy "Finds"

```python
elements = b.find_by_css('selector')

elements.first
elements.last
elements[1]  # slice
```

### Mouse

#### Eventos com mouse

O splinter nos ajuda a ter acesso a recursos do ActionChains (lowlevel) de maneira bem simples.

```python
caixa = b.find_by_id('caixa')

caixa.click()
caixa.mouse_over()    # AC
caixa.double_click()  # AC
caixa.right_click()   # AC
caixa.mouse_out()     # AC
```

Temos facilitadores para o click, assim como tínhamos com **fill**.

```python
b.click_link_href('href')
b.click_link_id('id')
b.click_link_text('text')
b.click_link_partial_text('text')

element = b.find_by_id('id')
element.check()
element.unckeck()
```


## Matchers

[Documentação](https://splinter.readthedocs.io/en/latest/matchers.html)

Matchers no splinter são um casamento entre duas funcionalidades. Os waits originais do selenium redesenhados e o esquema de assertivas que normalmente fazemos na mão.

Por exemplo, se quisermos saber, se um determinado texto está, ou não, na tela.

```python
from splinter import Browser

b = Browser()

b.visit('http://selenium.dunossauro.live/aula_09_a.html')

b.is_text_present('texto', wait_time=10)      # Boolean
b.is_text_not_present('texto', wait_time=10)  # Boolean
```

```python
from splinter import Browser

b = Browser()

b.visit('http://selenium.dunossauro.live/aula_09_a.html')

# is_element_present_by_*
# is_element_not_present_by_*
# * = seletor

b.is_element_present_by_css('i.dropped')  # Boolean
b.is_element_not_present_by_name('name')  # Boolean
```

Por exemplo, se quisermos saber,  se um determinado elemento está, ou não, na tela. (Somente XPATH e CSS selector).

```python
from splinter import Browser

b = Browser()

b.visit('http://selenium.dunossauro.live/aula_09_a.html')

b.is_element_visible_by_css('seletor')    # Boolean
b.is_element_visible_by_xpath('//xpath')  # Boolean
```


## Nem tudo são flores

- Não tem erros "explícitos"
- Não oferece suporte nativo a todos os browsers
  - Somente, Chrome e Firefox
  - [Writing New Drivers](https://splinter.readthedocs.io/en/latest/contribute/writing-new-drivers.html)
