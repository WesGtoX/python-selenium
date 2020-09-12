from selenium.webdriver import Remote
from sys import argv

browser = Remote(
    command_executor=f'http://{argv[-1]}:4444/wd/hub',
    desired_capabilities={'browserName':  'firefox'}
)

browser.get('http://selenium.dunossauro.live')

print(browser.page_source)
