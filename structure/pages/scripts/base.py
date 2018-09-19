from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# this Base class is serving basic attributes for every single page inherited from Page class
# driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
# driver.get("http://www.automationpractice.com/index.php")


class Page(object):
    def __init__(self, driver, base_url='http://automationpractice.com/index.php?'):
        self.base_url = base_url
        self._driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self._driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self._driver.get(url)

    def get_title(self):
        return self._driver.title

    def get_url(self):
        return self._driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self._driver).move_to_element(element)
        hover.perform()