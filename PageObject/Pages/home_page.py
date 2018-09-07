from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefo x)
from PageObject.Pages.locators import Locator
from PageObject.Pages.registration_page import Register

from PageObject.Pages.product_page import Product

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
        self.contactus = (By.XPATH, "//div[@id='contact-link']")
        self.singin = (By.XPATH, "//div[@class='header_user_info']")
        self.women = (By.XPATH, "//*[contains(text(), 'Women')]")
        self.search = (By.ID, "search_query_top")
        self.buttonsearch = (By.NAME, "submit_search")

        def getcontactus(self):
            return self.driver.find_element(*self.contactus)

        def getsingin(self):
            self.driver.find_element(*self.singin)
            self.singin.click()
            return Register(self.driver)

        def getwomen(self):
            return self.driver.find_element(*self.women)

        def setsearch(self, product):
            self.driver.find_element(*self.search)
            self.search.clear()
            self.search.send_keys(product)

        def getbuttonsearch(self):
            self.driver.find_element(*self.search)
            self.buttonsearch.click()
            return Product(self.driver)





 #   def getSingIn(self):
 #   return account