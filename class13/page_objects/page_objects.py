from abc import ABC


class SeleniumObject:

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)


class Page(ABC, SeleniumObject):

    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url
        self._reflection()

    def open(self):
        self.webdriver.get(self.url)

    def _reflection(self):
        for atribute in dir(self):
            real_atribute = getattr(self, atribute)
            if isinstance(real_atribute, PageElement):
                real_atribute.webdriver = self.webdriver


class PageElement(ABC, SeleniumObject):

    def __init__(self, webdriver=None):
        self.webdriver = webdriver
