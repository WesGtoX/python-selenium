"""
https://                  # schema
selenium.dunossauro.live  # netloc
/aula_04_b.html           # path
"""
from selenium.webdriver import Firefox
from urllib.parse import urlparse

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

parse_url = urlparse(browser.current_url)
