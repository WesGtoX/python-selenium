from splinter import Browser


b = Browser()

b.visit('http://selenium.dunossauro.live/aula_07.html')

b.find_by_id('nome').type('Fautinho')
b.find_by_id('email').type('faut@o.com')
b.find_by_id('senha').type('1234')
b.find_by_name('btn').click()
