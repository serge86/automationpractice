from selenium.webdriver.common.by import By

class Account:
    url = "http://automationpractice.com/index.php?controller=my-account"

    def __init__(self, driver):
        self._driver = driver

# registration page locators defining
        self.myaccount = (By.XPATH, "//*[@class='page-heading'][contains(text(),'My account')]") #"//span[text()='My account']"
        self.mywishlist = (By.XPATH, "//span[text()='My wishlists']")

    def get_my_account(self):
        return self._driver.find_element(*self.myaccount)

    def get_my_wishlist(self):
        return self._driver.find_element(*self.mywishlist)

    def get_url(self, url):
        return self._driver.get_url(url)
