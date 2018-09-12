from selenium.webdriver.common.by import By


from structure.pages.registration_page import Register

class Preregister:
    def __init__(self, driver):
        self._driver = driver

# registration page locators defining
        self.emailadress = (By.ID, "email_create")
        self.createanaccount = (By.ID, "SubmitCreate")
        self.errormessage = (By.XPATH, "//div[@class='alert alert-danger']")

    def setemailadress(self, email):
        self._driver.find_element(*self.emailadress).click()
        self._driver.find_element(*self.emailadress).clear()
        self._driver.find_element(*self.emailadress).send_keys(email)
        self._driver.find_element(*self.createanaccount).click()
        return Register(self)     

    def geterrormessage(self):
        return self._driver.find_element(*self.errormessage)


    # def getcreateanaccount(self):
    #     self.preregister.find_element(*self.createanaccount).click()
    #     #self.createanaccount.click()
    #     return Register(self)