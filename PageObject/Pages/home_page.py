from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefo x)
from PageObject.Pages.locators import Locator

driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
driver.get("http://www.automationpractice.com/index.php")
assert "My Store" in driver.title
elem = driver.find_element_by_id("search_query_top")
elem.clear()
elem.send_keys("women")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

class Home:

    def __init__(self, driver):
        self.driver = driver

#home page locator defining
        self.contactus = driver.find_element(*Locator.contactus)
        self.singin = driver.find_element(*Locator.singin)
        self.women = driver.find_element(*Locator.women)
        self.search = driver.find_element(*Locator.search)
        self.buttonsearch = driver.find_element(*Locator.search)

        def getcontactus(self):
            return self.contactus

        def getsingin(self):
            self.singin.click()
            return registration_page(self.driver)

        def getwomen(self):
            return self.women

        def setsearch(self, product):
            self.search.clear()
            self.search.send_keys(product)

        def getbuttonsearch(self):
            self.buttonsearch.click()
            return product_page(self.driver)





 #   def getSingIn(self):
 #   return account