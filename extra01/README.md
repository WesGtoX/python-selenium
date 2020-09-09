# Selenium + Behave

## Instação
```python
python -m venv ./venv
source venv/bin/activate    # Linux
\env\Scripts\activate.ps1   # Windows

pip install behave selenium
```


## Gerar arquivo requirements
`pip freeze > requirements.txt`


## Estrutura de diretórios
```bash
/
/features
/features/feature.gherkin
/features/environment.py

/features/steps
/features/steps/steps.py

/behave.ini
```

### O que vai dentro de cada arquivo?
| Arquivo        | O que vai dentro?                                  |
| -------------- | -------------------------------------------------- |
| *.feature      | Arquivo do gherking contendo as regras de execução |
| behave.ini     | Configurações do projeto                           |
| environment.py | Hooks do projeto                                   |
| /steps/*.py    | Arquivos com implementações dos steps              |


### Estrutura com projeto Page Objects
```bash
.
├── behave.ini
├── plain.output
├── README.md
├── reports
│   └── TESTS-todo.xml
└── todo_project
    ├── features
    │   ├── environment.py
    │   ├── steps
    │   │   └── todo.py
    │   └── todo.feature
    ├── page_objects
    │   ├── __init__.py
    │   └── page_objects.py
    └── pages
        ├── elements.py
        └── pages.py
```


## Documentação
- [Behave](https://behave.readthedocs.io/en/latest/)
- [Behave GitHub](https://github.com/behave/behave)