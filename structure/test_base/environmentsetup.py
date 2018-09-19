import unittest
import datetime
from selenium import webdriver


class EnvironmentSetup:

#setUp contains the browser setup attributes

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Drivers.chromedriver.exe")
        print("Run started at :"+str(datetime.datetime.now()))
        print("Chrome Enviroment Set Up")
        print("------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

#tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if (self.driver != None):
            print("-----------------------------------------")
            print("The Enviroment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()