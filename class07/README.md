# Aula 7 - Eventos Part I

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2307.pdf)

## DOM

- Inserir elementos
- Remover elementos

## CSSOM

- Alterar estilo
- Adicionar estilo


## Eventos

São super poderes que um Web Element adquirem pode ter para interagir com o usuário.

### Api de Eventos

Características importantes:

- Tipo (type) [nome]
- Alvo (target)

bubbles, cancelable, currentTarget, defaultPrevented, timestamp, istrusted, etc...

### Eventos que vamos estudar

- Foco (focus)
- Mudança (change)
- Mouse   |
- Drag     > Aula 08
- Teclado |

#### Focus x Blur

Quando o elemento é "acessado" ele está em foco. Com isso o evento "Focus" é disparado.

Quando o elemento perde o foco, o evento Blur é desencadeado

#### Change

O evento de mudança [change] é desencadeado quando um elemento perde o foco [blur]. 

O elemento será analisado e caso alguma mudança tenha ocorrido durante o período de foco, ele será disparado.


## Eventos + Selenium 

### Parte 1

#### Observando os eventos

A biblioteca do selenium conta com um mecanismo para observar eventos. Um EventListener [Escutador de eventos]. A implementação dele é baseada em um padrão de projeto chamado **Template Method**.

A ideia principal é fazer uma ação "antes" e/ou "depois" de alguma determinada ação do WebDriver


"Antes" e "Depois", geralmente são conhecidos como Hooks.Vamos usar o método 'click', como exemplo.

Estado anterior ---> WE < click > WE <-- Estado posterior

- EventListener  
    > O objetivo é observar o estado do WD em todos os momentos. Antes e depois de uma ação ser executada.
    > Quando ocorre o 'click' podemos observar o estado do dom, de um único elemento, fazer logs, etc...


## Event Firing

O disparador de eventos é uma "burocracia" do selenium para usar um Listener.

Ele constrói um wrapper do webdriver e dispara os eventos para o Listener.
