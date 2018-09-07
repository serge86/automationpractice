from PageObject.Pages.home_page import Home
from PageObject.Pages.registration_page import Register
from time import sleep
import pytest


class Automationpractice_registration():
    def tes_RegistrationFlow(self):
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php?")
        self.driver.set_page_load_timeout(20)

#calling home page object to click on Register Link
        home = Home(driver)
        if home.getRegister().is_displayed():
            print("Register Link displaying")
            home.getRegister().click()
            sleep(4)

#calling registrationn page object to proceed with registration flow
        reg = Register(driver)
        if reg.getsingin().is_displayed():
            print(reg.singin.text)
        else:
            print("Registration page not loaded")
