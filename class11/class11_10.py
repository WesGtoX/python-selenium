from selenium.webdriver import Firefox


url = 'https://selenium.dunossauro.live/aula_11_c.html'

browser = Firefox()

browser.get(url)

browser.execute_script('window.open("_blank")')

browser.switch_to.window(browser.window_handles[-1])

browser.get('https://ddg.gg')
