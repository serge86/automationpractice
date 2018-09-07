from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from automationpractice.PageOject.Pages.Locators import Locator


#driver = webdriver.Firefo x)
driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
driver.get("http://www.automationpractice.com/index.php")
assert "My Store" in driver.title
elem = driver.find_element_by_id("search_query_top")
elem.clear()
elem.send_keys("women")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

class Home(object):
    def __init__(self, driver):
        self.driver = driver

#home page locator
        self.contactus = driver.find_element(By.XPATH, Locator.contactus)
        self.singin = driver.find_element(By.XPATH, Locator.singin)
        self.women = driver.find_element(By.XPATH, Locator.women)

    def getSingIn(self):
    return account