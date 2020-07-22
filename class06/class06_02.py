from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()

b.get(url)

# usando o atributo type [attr=valor]
# name = b.find_element_by_css_selector('[type="text"]')
# password = b.find_element_by_css_selector('[type="password"]')
# btn = b.find_element_by_css_selector('[type="submit"]')

# usando o atributo name [attr=valor]
# name = b.find_element_by_css_selector('[name="nome"]')
# password = b.find_element_by_css_selector('[name="senha"]')
# btn = b.find_element_by_css_selector('[name="l0c0"]')

# # usando o atributo * [attr*=valor]
# name = b.find_element_by_css_selector('[name*="ome"]')
# password = b.find_element_by_css_selector('[name*="nha"]')
# btn = b.find_element_by_css_selector('[name*="l0"]')

# # usando o atributo | [attr|=valor]
# name = b.find_element_by_css_selector('[name|="nome"]')
# password = b.find_element_by_css_selector('[name|="senha"]')
# btn = b.find_element_by_css_selector('[name|="l0c0"]')

# usando o atributo ^ [attr^=valor]
name = b.find_element_by_css_selector('[name^="n"]')
password = b.find_element_by_css_selector('[name^="s"]')
btn = b.find_element_by_css_selector('[name^="l"]')

name.send_keys('Wesley')
password.send_keys('batatinhas123')
# btn.click()
