from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_06.html'

b = Firefox()

b.get(url)

input_l1c1 = b.find_element_by_css_selector('.form-l1c1 input[name="nome"]')
input_l1c1.send_keys('Wesley')
input_l0c0 = b.find_element_by_css_selector('.form-l0c0 input[name="nome"]')
input_l0c0.send_keys('Wesley')
input_l0c1 = b.find_element_by_css_selector('.form-l0c1 input[name="nome"]')
input_l0c1.send_keys('Wesley')
input_l1c0 = b.find_element_by_css_selector('.form-l1c0 input[name="nome"]')
input_l1c0.send_keys('Wesley')

b.find_elements_by_css_selector('form.form-l0c0 input')
b.find_elements_by_css_selector('form.form-l0c0 > div')

len(b.find_elements_by_css_selector('div.form-group'))
