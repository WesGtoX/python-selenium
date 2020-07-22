from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_06.html'

b = Firefox()

b.get(url)


b.find_element_by_css_selector('.form-l1c1 input[name="nome"]').send_keys('Wesley')
b.find_element_by_css_selector('.form-l0c0 input[name="nome"]').send_keys('Wesley')
b.find_element_by_css_selector('.form-l0c1 input[name="nome"]').send_keys('Wesley')
b.find_element_by_css_selector('.form-l1c0 input[name="nome"]').send_keys('Wesley')
b.find_elements_by_css_selector('form.form-l0c0 input')
b.find_elements_by_css_selector('form.form-l0c0 > div')
len(b.find_elements_by_css_selector('div.form-group'))
