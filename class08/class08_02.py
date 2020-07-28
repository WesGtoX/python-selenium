from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


url = 'https://selenium.dunossauro.live/aula_08_a'
text = 'Selenium'

browser = Firefox()
browser.get(url)

# hi-level
element = browser.find_element_by_name('texto')
# element.send_keys(text)

# low-level
ac = ActionChains(browser)
ac.move_to_element(element)
ac.click(element)


def type_with(key):
    ac.key_down(key)
    for letter in text:
        ac.key_down(letter)
        ac.key_up(letter)
    ac.key_up(u'\ue008')


type_with(Keys.SHIFT)
# type_with(u'\ue21EA')
# type_with(Keys.CAPS)

ac.perform()
