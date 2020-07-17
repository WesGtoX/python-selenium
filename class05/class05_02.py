from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_05_b.html'

firefox = Firefox()

firefox.get(url)

topic = firefox.find_element_by_class_name('topico')

languages = firefox.find_elements_by_class_name('linguagens')

for language in languages:
    print((language.find_element_by_tag_name('h2').text, language.find_element_by_tag_name('p').text))
