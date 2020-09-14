from selene.support.shared import browser
from selene.support.conditions import have


browser.open('http://selenium.dunossauro.live/aula_07')

# browser.element('input').should(be.blank).type('Envydust').press_enter()

browser.all('input').should(have.size(4))
