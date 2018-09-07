class Locator(object):

#home page locator
    contactus = '//div[@id="contact-link"]'
    singin = '//div[@class="header_user_info"]'
    women = "//*[contains(text(), 'Women')]"


from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

