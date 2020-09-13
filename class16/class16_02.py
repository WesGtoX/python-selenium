from splinter import Browser
from time import sleep

b = Browser()

b.visit('http://ddg.gg')

print(f'Título: {b.title}')
# print(f'html: {b.html}')
print(f'URL: {b.url}')

b.visit('http://google.com')
b.back()
sleep(3)
b.forward()
sleep(2)
b.quit()
