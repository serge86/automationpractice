from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
    contactus = (By.XPATH, '//div[@id="contact-link"]')
    singin = (By.XPATH, '//div[@class="header_user_info"]')
    women = (By.XPATH, "//*[contains(text(), 'Women')]")



class LoginPageLocatars(object):
  EMAIL         = (By.ID, 'ap_email')
  PASSWORD      = (By.ID, 'ap_password')
  SUBMIT        = (By.ID, 'signInSubmit-input')
  ERROR_MESSAGE = (By.ID, 'message_error')