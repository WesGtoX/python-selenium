from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_05_c.html'

firefox = Firefox()

firefox.get(url)

def best_movie(browser, movie, email, phone):
    """Preenche o formulário do melhor filme de 2020."""
    browser.find_element_by_name('filme').send_keys(movie)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(phone)
    firefox.find_element_by_name('enviar').click()

best_movie(firefox, 'Parasita', 'wesley@wesley.com', '(016)991993862')

firefox.quit()
