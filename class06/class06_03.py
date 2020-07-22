from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()

b.get(url)

b.find_element_by_css_selector('div.form-group')

b.find_elements_by_css_selector('div.form-group + br')[1].get_attribute('id')  # br irmão de div class form-group

# da tag div com a classe form-group pegue o filho com o id dentro-nome
b.find_element_by_css_selector('div.form-group > #dentro-nome')

# do form, pegue todas as tag label existentes ignorando a hierarquia (decendente)
b.find_elements_by_css_selector('form label')  
