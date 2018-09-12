from selenium import webdriver

class Ss:
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, path):
        directory = "D:\automationpractice\structure\screenshots"
        self.driver.get_screenshot_as_file(directory+path)