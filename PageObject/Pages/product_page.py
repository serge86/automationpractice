from PageObject.Pages.home_page import driver
from PageObject.Pages.locators import Locator
from selenium.webdriver.support.select import Select

class Product:
    def __init__(self, driver):
        self.driver = driver