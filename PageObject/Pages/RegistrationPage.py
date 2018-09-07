import self as self
from automationpractice.PageOject.Pages.Locators import Locator
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Register(object):
    def __init__(selfself, driver):
        self.driver = driver

# registration page locators defining, you can directly call WebElement from here
    self.