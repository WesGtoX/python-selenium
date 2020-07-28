import re

from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/caixinha'

browser = Firefox()
browser.get(url)

box = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)


color_list = []


def get_color(text):
    text = re.search('(?<=cor:")([a-z]+)', text).group(0)
    if text not in color_list:
        color_list.append(text)


def show_colors(browser):
    element_list = browser.find_element_by_css_selector('textarea').text
    element_list = element_list.split('\n')
    [get_color(color) for color in element_list if color not in color_list]
    print(f'Todas as cores possívels: {[color for color in color_list]}')


def color_box(ac, key1=None, key2=None):
    if key1:
        ac.key_down(key1)

    if key2:
        ac.key_down(key2)

    ac.move_to_element(box)
    ac.click()
    ac.double_click()
    ac.move_to_element(span)

    if key1:
        ac.key_up(key1)

    if key2:
        ac.key_up(key2)


color_box(ac)
color_box(ac, Keys.SHIFT)
color_box(ac, Keys.CONTROL)
color_box(ac, Keys.SHIFT, Keys.CONTROL)

ac.move_to_element(box)
ac.context_click()
ac.perform()

show_colors(browser)
