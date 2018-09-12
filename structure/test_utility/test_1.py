from structure.pages.home_page import Home, driver
from selenium import webdriver

from structure.pages.my_account_page import Account
from structure.pages.preregistration_page import Preregister
from structure.pages.product_page import Product
from structure.pages.registration_page import Register


home = Home(driver)
product = Product(driver)
preregister = Preregister(driver)
register = Register(driver)
account = Account(driver)


def setUp(self):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.driver.get("http://www.automationpractice.com/index.php")


def test_check_search():
    home.setsearch("woman")
    product.getsortby()
    assert product.getsortby().is_displayed()
    driver.close()


def test_invalid_email():
    home.getsingin()
    preregister.setemailadress("fgdfgdfgd")
    assert preregister.geterrormessage().is_enabled()
    driver.close()


def test_preregistration():
    home.getsingin()
    preregister.setemailadress("778@gmail.com")
    driver.implicitly_wait(20)
    assert register.getinformation().is_enabled()
    driver.close()

def test_create_account():
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation")
    preregister.setemailadress("800@gmail.com")
    driver.implicitly_wait(20)
    register.getmr()
    driver.implicitly_wait(20)
    register.setfirstname("Vano")
    register.setlastname("Petrov")
    register.setemail("555@gmail.com")
    register.setpassword("98765")
    register.getday("7")
    driver.implicitly_wait(30)
    register.getmonth("11")
    driver.implicitly_wait(30)
    register.getyear("1955")
    register.setaddress("MMM")
    register.setcity("London")
    driver.implicitly_wait(30)
    register.getstate("6")
    driver.implicitly_wait(30)
    register.setpostcode("54321")
    driver.implicitly_wait(20)
    register.getcountry("United States")
    driver.implicitly_wait(20)
    register.setmobilephone("256897412")
    driver.implicitly_wait(20)
    register.setalias("555@gmail.com")
    driver.implicitly_wait(20)
    register.getregisterbutton()
    assert account.getmyaccount().is_displayed
    #assert account.get_url("http://automationpractice.com/index.php?controller=my-account")._driver.current_url
    driver.close()

def test_create_existing_account():
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation")
    preregister.setemailadress("778@gmail.com")
    driver.implicitly_wait(20)
    register.getmr()
    driver.implicitly_wait(20)
    register.setfirstname("Ivan")
    register.setlastname("Popov")
    register.setemail("444@gmail.com")
    register.setpassword("12345")
    driver.implicitly_wait(30)
    register.getday("8")
    driver.implicitly_wait(30)
    register.getmonth("12")
    driver.implicitly_wait(30)
    register.getyear("1905")
    register.setaddress("AAAA")
    register.setcity("Lviv")
    driver.implicitly_wait(30)
    register.getstate("6")
    driver.implicitly_wait(30)
    register.setpostcode("56789")
    driver.implicitly_wait(20)
    register.getcountry("United States")
    driver.implicitly_wait(20)
    register.setmobilephone("123456789")
    driver.implicitly_wait(20)
    register.setalias("444@gmail.com")
    driver.implicitly_wait(20)
    register.getregisterbutton()
    assert register.getaccount_error_message().is_enabled()
    driver.close()

def tearDown(self):
    self.driver.quit()
