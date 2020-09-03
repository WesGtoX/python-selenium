from selenium.webdriver import Firefox
from pages.pages import PageTodo


browser = Firefox()
url = 'https://selenium.dunossauro.live/todo_list.html'

"""
Cenário: Criar um cartão
    Dado que esteja na página de todo
    Quando criar um todo
    Então o cartão deve estar na pilha "A fazer"

Cenário: Mover cartão para fazendo
    Dado que esteja na página de todo
    Quando criar um todo
    E mover o todo para fazendo
    Então o cartão deve estar na pilha "Fazendo"
"""

print('Dado que esteja na página de todo')
todo_page = PageTodo(browser, url)

todo_page.open()

print('Quando criar um todo')
todo_page.todo.create_todo(
    'POM', 'POM POM POMMMMMMM'
)

print('Então o cartão deve estar na pilha "A fazer"')
first_todo = todo_page.a_fazer.todos[0]
assert first_todo.name == 'POM'
assert first_todo.description == 'POM POM POMMMMMMM'


print('----------------------------------------------')


print('Dado que esteja na página de todo')
todo_page = PageTodo(browser, url)

todo_page.open()

print('Quando criar um todo')
todo_page.todo.create_todo(
    'POM', 'POM POM POMMMMMMM'
)

print('E mover o todo para fazendo')
first_todo = todo_page.a_fazer.todos[0]
first_todo.do()

print('Então o cartão deve estar na pilha "Fazendo"')
first_todo = todo_page.doing.todos[0]
assert first_todo.name == 'POM'
assert first_todo.description == 'POM POM POMMMMMMM'

browser.quit()
