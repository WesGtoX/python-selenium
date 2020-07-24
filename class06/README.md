# Aula 6 - Procurando e interagindo com elementos Part II

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2306.pdf)

## Um pouco de teoria dos seletores

São maneiras de encontrar elemnetos dentro de uma estrutura HTML/XML que tem uma sintaxe própria e nomenclatura própria, ele da nomes e tem uma sintaxe de uma forma diferente.

É uma maneira de selecionar elementos usando os atributos dos próprios elementos.


## CSS selector

- Básicos
  - ID
    ```
    >>> b.find_element_by_css_selector(‘#python’)
    >>> b.find_element_by_css_selector(‘#haskell’)
    >>> b.find_element_by_css_selector(‘#lisp’)
    ```
  - Tipo [tag]
    ```
    >>> b.find_element_by_css_selector(‘form’)
    >>> b.find_element_by_css_selector(‘div’)
    >>> b.find_element_by_css_selector(label)

    >>> b.find_elementS_by_css_selector(‘div’)
    ```
  - Classe
    ```
    >>> b.find_element_by_css_selector(‘.form-group’)  # As classe para o css são delimitadas por [.].classe
    >>> b.find_elementS_by_css_selector(‘div.form-group’)  # Também posso especificar a tagtag.classe
    ```
  - Atributo
    | Operador |          Significado           |
    | :------: | :----------------------------: |
    |    =     |   Deve ser exatamente igual    |
    |    *=    |        Deve ocorrer em         |
    |   \|=    | Deve ser exatamente ou iniciar |
    |    ^=    |          Iniciado em           |
    |    $=    |          Terminado em          |
    |    ~=    |  Um deve ser exatamente igual  |

    ```
    >>> b.find_elementS_by_css_selector(‘[for]’)
    >>> b.find_elementS_by_css_selector(‘[type]’)

    >>> b.find_elementS_by_css_selector(‘[for]’)
    >>> b.find_elementS_by_css_selector(‘[type]’)
    >>> b.find_elementS_by_css_selector(‘[name]’)

    >>> b.find_elementS_by_css_selector(‘[class="form-group"]’)  # Todos atributos class em que o valor seja exatamente igual a form-group

    >>> b.find_elementS_by_css_selector(‘[class*="group"]’)  # Todos atributos class em que a palavra group exista
    
    >>> b.find_elementS_by_css_selector(‘[type$="t"]’)  # Todos os atributos type que o final do valor seja t
    ```
  - Universal
    ```
    >>> b.find_elementS_by_css_selector(‘*’)
    ```
  - Combinados
    ```
    >>> b.find_elementS_by_css_selector(‘input[type$="t"]’)  # Todos as tags input com atributos type que o final do valor seja t
    
    >>> b.find_elementS_by_css_selector(‘label[for*="n"]’)  # Todos as tags label onde os atributos for contenham n

    >>> b.find_elementS_by_css_selector(‘*[for*="n"]’)  # Qualquer tag onde os atributos for contenham nequivalente a [for*="n"]
    ```
- Seletores de Grupo
  - Lista de seletores
    ```
    >>> b.find_elementS_by_css_selector(‘label, input’)  # Encontra qualquer tag labeljuntamente a qualquer tag type
    >>> b.find_elementS_by_css_selector(‘label[for], *[type$=”t”]’)  # Encontra qualquer tag label que contenha o atributo forjuntamente a quaisquer tags (*) que tenham o atributo type com valor que termine em tv
    ```
- Combinadores
  - Irmãos adjacentes   (A + B)
    ```
    >>> b.find_elementS_by_css_selector(‘fausto[cara=”triste”] + vara’)
    >>> b.find_elementS_by_css_selector(‘div + br’)  # Encontra qualquer br após uma div
    >>> b.find_element_by_css_selector(‘h2 + div’)  # Encontra a primeiro div após uma h2
    >>> b.find_elementS_by_css_selector(mago ~ fausto’)
    >>> b.find_elementS_by_css_selector(‘h2 ~ div’)  # Encontra todas as tags div que estejam no mesmo nível de h2
    >>> b.find_elementS_by_css_selector(‘h2 ~ br’)  # Encontra todas as tags br que estejam no mesmo nível de h2
    ```
  - Geral de irmãos     (A ~ B)
  - Filhos              (A > B)
  ```
  >>> b.find_elementS_by_css_selector(‘mago > fausto’)
  >>> b.find_elementS_by_css_selector(‘div > br’)  # Encontra todas as tags br que sejam filhas de div
  ```
  - Descendentes        (A   B)
  ```
  >>> b.find_elementS_by_css_selector(fausto[nome=”faustão”] fausto’)
  >>> b.find_elementS_by_css_selector(‘form br’)  # Encontra todas as tags br que sejam filhas de form direta ou indiretamente
  ```
- Pseudo [classes, elementos] <- Não vamos falar sobre