# Aula 8 - Eventos Part II

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2308.pdf)

## Eventos

### Teclado

Existem 3* tipos de eventos disparados por teclado
- keyup
- keydown
- accesskey
- keypress (obsoleto)


Três atributos considerados mais importantes:

- key (Valor da tecla)
- Atributos de teclas
  - shiftKey
  - altKey
  - metaKey
  - ctrlKey
- getModifierState()
  - CapsLock
  - shift
  - meta
  - os

Selenium + Eventos

Eventos, em grande maioria, dependem de interações do usuário.
Ppodemos interagir com o browser de várias maneiras:

- Mouse
- Teclado
- Touch*
- ...


### Mouse

Tipos de eventos disparados por teclado
- mouseenter
- mouseleave
- click
- dblclick
- contextmenu

Atributos de ação
- shiftKey
- altKey
- metaKey
- ctrlKey


### Drag and Drop

[Drag and Drop [Python] #8345](https://github.com/SeleniumHQ/selenium/issues/8345)


## ActionChains

Low-level API

São maneiras de automatizar ações de baixo nível.

Por exemplo, como uma tecla é pressionada?
- key Down
- key Up

Descrevendo ações
- Hi-level
  1. nome = browser.find_element_by_id(‘nome’)
  2. nome.send_keys(‘eduardo’)

- Low-level

1. nome = find_element(by.ID, 'nome')  
2. move_to_element(nome)
    - key_down('e')
    - key_up('e')
    - key_down('d')
    - key_up('d')
    - key_down('u')
    - ...
