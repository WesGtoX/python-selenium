from page_objects import Page
from .elements import AFazer, Doing, Done, Todo


class PageTodo(Page):
    a_fazer = AFazer()
    doing = Doing()
    done = Done()
    todo = Todo()
