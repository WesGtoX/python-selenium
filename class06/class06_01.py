from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()

b.get(url)

b.find_element_by_css_selector('input').send_keys('Wesley')
