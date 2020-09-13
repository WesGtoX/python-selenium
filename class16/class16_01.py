from splinter import Browser


# b = Browser()  # Firefox
# b = Browser(headless=True)  # O browser não abre visivelmente
# b.visit('http://ddg.gg')
# print(b.html)
# b.quit()

# b = Browser(incognito=True)  # Modo privato
# b = Browser(headless=True, incognito=True)
# b.quit()

# b = Browser('chrome', incognito=True)
# b = Browser('firefox', incognito=True)

# b = Browser('opera', incognito=True)  # Não tem suporte padrão

b = Browser(
    driver_name='remote',
    browser='firefox',
)
