from selenium.webdriver import Firefox
from pages.pages import PageTodo


browser = Firefox()
url = 'https://selenium.dunossauro.live/todo_list.html'

# Arange ---------------------------------------------
todo_page = PageTodo(browser, url)

todo_page.open()

# Act ------------------------------------------------
todo_page.todo.create_todo(
    'POM', 'POM POM POMMMMMMM'
)

# Assert ---------------------------------------------
first_todo = todo_page.a_fazer.todos[0]
assert first_todo.name == 'POM'
assert first_todo.description == 'POM POM POMMMMMMM'

browser.quit()
