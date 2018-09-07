
from PageObject.Pages.home_page import driver
from PageObject.Pages.locators import Locator
from selenium.webdriver.support.select import Select
from self import self


class Register:
    def __init__(self, driver):
        self.driver = driver

# registration page locators defining, you can directly call WebElement from here
    self.emailadress = driver.find_element(*Locator.emailadress)
    self.createanaccount = driver.find_element(*Locator.createanaccount)
    self.mr = driver.find_element(*Locator.mr)
    self.firstname = driver.find_element(*Locator.firstname)
    self.lastname = driver.find_element(*Locator.lastname)
    self.email = driver.find_element(*Locator.email)
    self.password = driver.find_element(*Locator.password)
    self.day = driver.find_element(*Locator.day)
    self.month = driver.find_element(*Locator.month)
    self.year = driver.find_element(*Locator.year)
    self.address = driver.find_element(*Locator.address)
    self.city = driver.find_element(*Locator.city)
    self.state = driver.find_element(*Locator.state)
    self.postcode = driver.find_element(*Locator.postcode)
    self.country = driver.find_element(*Locator.country)
    self.mobilephone = driver.find_element(*Locator.mobilephone)
    self.alias = driver.find_element(*Locator.alias)
    self.registerbutton = driver.find_element(*Locator.registerbutton)

#you can return WebElement from method and call it also, and useful methob with parametr you define here

    def setemailadress(self, email):
        self.emailadress.click()
        self.emailadress.clear()
        self.emailadress.send_keys(email)

    def getcreateanaccount(self):
        self.createanaccount.click()
        return my_account_page(self.driver)

    def getmr(self):
        self.mr.click()

    def setfirstname(self, Name):
        self.firstname.click()
        self.firstname.clear()
        self.firstname.send_keys(Name)

    def setlastname(self, Name):
        self.lastname.click()
        self.lastname.clear()
        self.lastname.send_keys(Name)

    def setemail(self, email):
        self.email.click()
        self.email.clear()
        self.email.send_keys(email)

    def setpassword(self, password):
        self.password.click()
        self.password.clear()
        self.password.send_keys(password)

    def setday(self, day):
        select = Select(self.day)
        select.select_by_visible_text(day)
        self.day.click()

    def getmonth(self, month):
        select = Select(self.month)
        select.select_by_visible_text(month)
        self.month.click()

    def getyear(self, year):
        select = Select(self.year)
        select.select_by_visible_text(year)
        self.year.click()

    def setaddress(self, address):
        self.address.clear()
        self.address.send_keys(address)

    def setcity(self, city):
        self.city.clear()
        self.city.send_keys(city)

    def getstate(self, state):
        select = Select(self.state)
        select.select_by_visible_text(state)
        self.state.click()

    def setpostcode(self, postcode):
        self.postcode.clear()
        self.postcode.send_keys(postcode)

    def getcountry(self, country):
        select = Select(self.country)
        select.select_by_visible_text(country)
        self.country.click()

    def setmobilephone(self, mobilephone):
        self.mobilephone.clear()
        self.mobilephone.send_keys(mobilephone)

    def setalias(self, email):
        self.alias.clear()
        self.alias.send_keys(email)

    def getregisterbutton(self,):
        self.registerbutton.click()
        return my_account_page(self.driver)



