from selenium.webdriver import Firefox


browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

unordered_list = browser.find_element_by_tag_name('ul')  # 1

lis = unordered_list.find_elements_by_tag_name('li')  # 2

print(lis[0].find_element_by_tag_name('a').text)  # 3


"""
1. Buscamos 'ul'
2. Buscamos todos 'li'
3. No primeiro 'li', buscamos 'a'

ul
  li
    a
      text
  li
    a
      text

"""
