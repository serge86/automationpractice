from selenium import webdriver
from selenium.webdriver.common.by import By
# #driver = webdriver.Firefo x)
from structure.pages.preregistration_page import Preregister
from .product_page import Product


driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
driver.get("http://www.automationpractice.com/index.php")


class Home:

    def __init__(self, driver):
        """
        
        :param driver:
        """
        self._driver = driver


#home page locator defining
        self.contactus = (By.XPATH, "//div[@id='contact-link']")
        self.singin = (By.XPATH, "//div[@class='header_user_info']")
        self.women = (By.XPATH, "//*[contains(text(), 'Women')]")
        self.search = (By.ID, "search_query_top")
        self.buttonsearch = (By.NAME, "submit_search")

    def getcontactus(self):
        return self._driver.find_element(*self.contactus)

    def getsingin(self):
        self._driver.find_element(*self.singin).click()
        return Preregister(self)

    def getwomen(self):
        return self._driver.find_element(*self.women)

    def setsearch(self, product):
        self._driver.find_element(*self.search).clear()
        self._driver.find_element(*self.search).send_keys(product)
        self._driver.find_element(*self.buttonsearch).click()
        return Product(self)



