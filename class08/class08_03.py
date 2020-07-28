from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


url = 'https://selenium.dunossauro.live/caixinha'

browser = Firefox()
browser.get(url)

box = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)


def color_box(key1=None, key2=None):
    ac.pause(1)
    if key1:
        ac.key_down(key1)

    if key2:
        ac.key_down(key2)

    ac.move_to_element(box)
    ac.pause(1)
    ac.click()
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(span)
    ac.pause(1)

    if key1:
        ac.key_up(key1)

    if key2:
        ac.key_up(key2)


color_box()
color_box(Keys.SHIFT)
color_box(Keys.CONTROL)
color_box(Keys.SHIFT, Keys.CONTROL)

ac.pause(1)
ac.move_to_element(box)
ac.context_click()
ac.pause(1)
ac.perform()
