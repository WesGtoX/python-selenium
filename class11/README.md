# Aula 11 - Janelas, frames e coisas mais

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2311.pdf)


## Alertas

Alertas são elementos relativos as janelas. São elementos que não estão necessariamente presentes no DOM.

Existem 3 tipos de "alertas" e cada um tem sua maneira própria de interação com o selenium
- alert
- prompt
- confirm

### Waits em alerts

Como tudo, temos possíveis problemas com possíveis tempos.

Existe uma condição pronta para alertas e ela ainda retorna o alerta para facilitar.


## Janelas e Abas

```
ABAS = JANELAS
POPUPS = JANELAS
```

### Abrindo abas

Abrindo abas usando script:
```python
browser.execute_script('window.open("_blank")')
browser.switch_to.window(browser.window_handles[-1])
browser.get('https://ddg.gg')
```

### Esperas para janelas
- EC
  - Uma janela nova?
  - O número de janelas deve ser?


## iFrames

### Waits Iframes
- EC
  - Tem um frame disponível?