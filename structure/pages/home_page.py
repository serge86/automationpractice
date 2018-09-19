# pylint: disable=too-many-instance-attributes
from selenium import webdriver
from selenium.webdriver.common.by import By
from structure.pages.preregistration_page import Preregister
from .product_page import Product

driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
driver.get("http://www.automationpractice.com/index.php")


class Home:
    """
    Class that describes the home page
    of the website
    """

    def __init__(self, driver):
        """

        :param driver: Driver to use
        """
        self._driver = driver

        # home page locator defining
        self.contact_us = (By.XPATH, "//div[@id='contact-link']")
        self.sing_in = (By.XPATH, "//div[@class='header_user_info']")
        self.women = (By.XPATH, "//*[contains(text(), 'Women')]")
        self.search = (By.ID, "search_query_top")
        self.button_search = (By.NAME, "submit_search")

    def get_contact_us(self):
        """Takes an element using web driver

        :return: web element contactus
        """
        return self._driver.find_element(*self.contact_us)

    def get_sing_in(self):
        """Takes an element using web driver

        :return: preregistration_page
        """
        self._driver.find_element(*self.sing_in).click()
        return Preregister(self)

    def get_women(self):
        """Takes an element using web driver

        :return: web element women
        """
        return self._driver.find_element(*self.women)

    def set_search(self, product):
        """Find the field using web driver, clears it
        and provides the param, make a click

        :param product: is a object on product_page
        :return: product_page
        """
        self._driver.find_element(*self.search).clear()
        self._driver.find_element(*self.search).send_keys(product)
        self._driver.find_element(*self.button_search).click()
        return Product(self)


class User:
    """
    This class have properties of user
    """

    def __init__(self, first_name, last_name, email, password, day, month, year, address,
                 city, state, post_code, country, mobile_phone, alias):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.day = day
        self.month = month
        self.year = year
        self.address = address
        self.city = city
        self.state = state
        self.post_code = post_code
        self.country = country
        self.mobile_phone = mobile_phone
        self.alias = alias
