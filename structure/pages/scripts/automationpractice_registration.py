
from time import sleep
import pytest
from _pytest import unittest

from structure.pages.preregistration_page import Preregister
#from ..home_page import Home
from ..home_page import Register, Home


class Automationpractice_registration():
    def test_RegistrationFlow(self):
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php?")
        self.driver.set_page_load_timeout(20)

#calling home page object to click on Contcat us Link
        home = Home(driver)
        if home.getcontactus().is_displayed():
            print("Contact us Link displaying")
            self.assertTrue(page.home_page_loaded())
            sleep(4)

 # calling home page object to click on Sing in Link
        home = Home(driver)
        if home.getsingin().is_displayed():
                print("Sing in Link displaying")
                home.getsingin().click()
                sleep(4)

#calling registrationn page object to proceed with registration flow
        prereg = Preregister(driver)
        if prereg.getsingin().is_displayed():
            print(prereg.singin.text)
        else:
            print("Registration page not loaded")
        try:
            prereg.setmailadress(self, 777@gmail.com)
            prereg.getcreateanaccount()
        except Exception as e:
            print("Exeption occured "+e)

if __name__ == '__main__':
    unittest.main

