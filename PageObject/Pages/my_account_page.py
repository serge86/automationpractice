from PageOject.locators import Locator
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver




class Register:
    def __init__(self, driver):
        assert isinstance(driver, )
        self.driver = driver

# registration page locators defining
    self.myaccount = driver.find_element(*Locator.myaccount)
    self.mywishlist = driver.find_element(*Locator.mywishlists)

