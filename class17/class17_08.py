from selene.support import by
from selene.support.shared import browser
from selene.support.conditions import be, not_


browser.open('http://google.com')

browser.s(by.name('q')).should(be.blank).type('Live de Python')

browser.s(by.name('q')).should(not_.blank).type('100')
