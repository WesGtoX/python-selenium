# Exercício 02
# Crie um programa com selenium que
# - Jogue o jogo
# - Quando você ganhar o script deve parar de ser executado
# url: https://curso-python-selenium.netlify.app/exercicio_02.html

from selenium.webdriver import Firefox
from time import sleep


url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()
browser.get(url)

sleep(1)

a = browser.find_element_by_tag_name('a')

expected_number = browser.find_elements_by_tag_name('p')

number = '-1'
while number in expected_number[-1].text:
    a.click()
    random_number = browser.find_elements_by_tag_name('p')
    number = random_number[-1].text

end_game = browser.find_elements_by_tag_name('p')
print(end_game[-1].text)

browser.quit()
