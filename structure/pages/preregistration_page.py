from selenium.webdriver.common.by import By


from structure.pages.registration_page import Register


def Preregister():
    pass


class Preregister:

    def __init__(self, driver):
        self._driver = driver

# registration page locators defining
        self.emailadress = (By.ID, "email_create")
        self.createanaccount = (By.ID, "SubmitCreate")
        self.errormessage = (By.XPATH, "//div[@class='alert alert-danger']")

    def set_email_adress(self, email):
        self._driver.implicitly_wait(20)
        self._driver.find_element(*self.emailadress).click()
        self._driver.implicitly_wait(20)
        self._driver.find_element(*self.emailadress).clear()
        self._driver.find_element(*self.emailadress).send_keys(email)
        self._driver.find_element(*self.createanaccount).click()
        return Register(self._driver)

    def get_error_message(self):
        return self._driver.find_element(*self.errormessage)


    # preregister = Preregister()
    #
    # preregister.set_email_adress()