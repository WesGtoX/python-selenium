# Aula 10 - Waits Part II

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2310.pdf)

## Expected conditions

[DOC](https://www.selenium.dev/selenium/docs/api/py/_modules/selenium/webdriver/support/expected_conditions.html)

São classes prontas para esperas "comuns", "usuais".. Divididas por categoria (Não oficial).

- Existência do elemento
- Visibilidade do elemento
- Navegação
- Verificação de texto
- Janelas e frames

### Existência do elemento

Saber se o elemento está na tela, talvez o tipo de espera mais comum.

Evita de tentar executar uma operação em um elemento que pode ainda não estar disponível.

### Visibilidade do elemento

Basicamente queremos saber se o elemento está desenhado na tela ou não (aula de drawing/eventos) e também se ele está ativo ou não.

Exemplos:

- O elemento pode não ter sido desenhado
- O elemento pode ter sido desenhado mas estar inativo


## Navegação

Esperas baseadas em navegação


## Verificação de texto

Esperas por texto
