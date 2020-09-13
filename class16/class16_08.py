from splinter import Browser


b = Browser()

b.visit('http://selenium.dunossauro.live/caixinha.html')

box = b.find_by_id('caixa')

box.click()

# AC
box.mouse_over()
box.double_click()
box.right_click()
# box.mouse_out()
