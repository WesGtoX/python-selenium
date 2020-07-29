# Aula 9 - Waits Part I

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2309.pdf)

## Carregamento da página
- Normal
- Async
- Defer


## Wait

### Tipos de esperas


- Implícitas
  - Espera todos os elementos, eventos, navegação, com um tempo padrão
- Explícitas
  - Selenium disponibiliza um range de waits prontos
  - Customizável
    - Em tipos de espera
    - É possível criar suas próprias esperas
  - Reutilizável

#### Wait implícito

- Prós
  - Funciona em cenários Flaky
  - Não se preocupe, nós vamos esperar

- Contras
  - Segura a aplicação por mais tempo
  - Tudo é esperado tendo o mesmo tempo como base
  - Não funciona para elementos específicos
  - Se algo der errado, vai demorar o tempo do wait para saber

#### WebDriverWait

```python
from selenium.webdriver.support.ui import WebDriverWait

wdw = WebDriverWait(
  driver,  # WebDriver
  timeout,  # Tempo de espera até o erro (segundos)
  poll_frequency=0.5,  # Tempo entre uma tentativa e outra
  ignored_exceptions=None  # Lista de coisas que vamos ignorar
)
```

- WebDriverWait [until]

  Executa até que o `Callable` retorne `True`, ou até estourar o `timeout` de wdw.

  ```python
  wdw.until(
    Callable,  # Operação que vai ser executada
    message,  # Mensagem caso o erro ocorra
  )
  ```

- WebDriverWait [until_not]

  Executa até que o `Callable` retorne `False`, ou até estourar o `timeout` de wdw.

  ```python
  wdw.until_not(
    Callable,  # Operação que vai ser executada
    message,  # Mensagem caso o erro ocorra
  )
  ```

### Functools Partial

#### Parametrizando esperas

Fizemos esperas "especializadas". Isso é complicado, pois todo código precisa ser feito "mais de uma vez".

A solução é adicionar um novo parâmetro


## By

O By nos auxilia a deixar o código mais "assertivo". Ele é comumente usado em conjunto o `wb.find_element`. Assim nos ajuda a parametrizar mais as nossas funções.


## Esperas com classes

### Para fãs de OO

Aqui evitamos o uso do partial usando `__call__`.

Não é a minha abordagem preferida, mas é a tradicional em relação a lib.

```python
class WaitElement:

    def __init__(self, by, selector):
        self.locator = (by, selector)

    def __call__(self, driver):
        if web_driver.find_elements(*self.locator):
            return True
        return False


web_driver_wait.until(WaitElement(By.ID, 'meu_id'))
```

## Locators

Locators são maneiras de unir o By a string do elemento.

Porém esse conceito é trazido do selenium java e faz pouco ou nenhum sentido usando em python.

Resumidamente um Locator é uma tupla com o By e a string do elemento.

```python
from selenium.webdriver.common.by import By


locator = (By.CSS_SELECTOR, 'div.minha_classe')
```


## Esperando elemento ativo

Embora seja possível ver o elemento, ele não tem as características que precisamos para clicar.

Precisamos esperar o elemento estar ativo is_enabled
