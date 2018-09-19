import pytest
from structure.pages.home_page import Home, driver, User
from selenium import webdriver
from structure.pages.my_account_page import Account
from structure.pages.preregistration_page import Preregister
from structure.pages.product_page import Product
from structure.pages.registration_page import Register


@pytest.fixture()
def setUp(self):
    self.driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
    self.driver.get("http://www.automationpractice.com/index.php")


home = Home(driver)
product = Product(driver)
preregister = Preregister(driver)
register = Register(driver)
account = Account(driver)
url = Register.url

user = User("Ivan", "Popov", "227@gmail.com", "12345", "8", "12",
            "1905", "AAAA", "Lviv", "6", "56789", "United States", "123456789", "227@gmail.com")


@pytest.fixture()
def tearDown(self):
    self.driver.quit()