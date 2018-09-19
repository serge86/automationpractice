from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from structure.pages.my_account_page import Account


class Register:
    url = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"

    def __init__(self, driver):
        self._driver = driver

# registration page locators defining, you can directly call WebElement from here
        #self.information = (By.XPATH, "//h3[contains (text(),'Your personal information')]")
        #self.information = (By.XPATH, "//*[contains(text(), 'Your personal information')]")
        self.information = (By.XPATH, "//*[@class='page-heading'][contains(text(),'Create an account')]")
        self.mr = (By.ID, "uniform-id_gender1")
        self.mrs = (By.ID, "uniform-id_gender2")
        self.firstname = (By.ID, "customer_firstname")
        self.lastname = (By.ID, "customer_lastname")
        self.email = (By.ID, "email")
        self.password = (By.ID, "passwd")
        self.day = (By.ID, "days")
        self.month = (By.ID, "months")
        self.year = (By.ID, "years")
        self.address = (By.ID, "address1")
        self.city = (By.ID, "city")
        self.state = (By.ID, "id_state")
        self.postcode = (By.ID, "postcode")
        self.country = (By.ID, "id_country")
        self.mobilephone = (By.ID, "phone_mobile")
        self.alias = (By.ID, "alias")
        self.registerbutton = (By.ID, "submitAccount")
        self.account_error_message = (By.XPATH, "//*[contains(text(), 'There is 1 error')]")

#you can return WebElement from method and call it also, and useful methob with parametr you define here
    def get_url(self, url):
        return self._driver.get_url(url)

    def get_information(self):
        return self._driver.find_element(*self.information)

    def get_mr(self):
        self._driver.implicitly_wait(20)
        self._driver.find_element(*self.mr).click()
    
    def is_mr_radio_button_selected(self, element):
        return self._driver.find_element(*self.mr, element)

    def get_mrs(self):
        return self._driver.find_element(*self.mrs)

    def set_first_name(self, first_name):
        self._driver.find_element(*self.firstname).click()
        self._driver.find_element(*self.firstname).clear()
        self._driver.find_element(*self.firstname).send_keys(first_name)

    def set_last_name(self, last_name):
        self._driver.find_element(*self.lastname).click()
        self._driver.find_element(*self.lastname).clear()
        self._driver.find_element(*self.lastname).send_keys(last_name)

    def set_email(self, email):
        self._driver.find_element(*self.email).click()
        self._driver.find_element(*self.email).clear()
        self._driver.find_element(*self.email).send_keys(email)

    def set_password(self, password):
        self._driver.find_element(*self.password).click()
        self._driver.find_element(*self.password).clear()
        self._driver.find_element(*self.password).send_keys(password)

    def get_day(self, value):
        select_day = Select(self._driver.find_element_by_id("days"))
        select_day.select_by_value(value)        

    def get_month(self, value):
        select_month = Select(self._driver.find_element_by_id("months"))
        select_month.select_by_value(value)        

    def get_year(self, value):
        select_year = Select(self._driver.find_element_by_id("years"))
        select_year.select_by_value(value)    

    def set_address(self, address):
        self._driver.find_element(*self.address).clear()
        self._driver.find_element(*self.address).send_keys(address)

    def set_city(self, city):
        self._driver.find_element(*self.city).clear()
        self._driver.find_element(*self.city).send_keys(city)
    
    def get_state(self, value):
        select_st = Select(self._driver.find_element_by_id("id_state"))
        select_st.select_by_value(value)
        
    def set_post_code(self, post_code):
        self._driver.find_element(*self.postcode).clear()
        self._driver.find_element(*self.postcode).send_keys(post_code)

    def get_country(self, text):
        select_cou = Select(self._driver.find_element_by_id("id_country"))
        select_cou.select_by_visible_text(text)

    def set_mobile_phone(self, mobile_phone):
        self._driver.find_element(*self.mobilephone).clear()
        self._driver.find_element(*self.mobilephone).send_keys(mobile_phone)

    def set_alias(self, alias):
        self._driver.find_element(*self.alias).clear()
        self._driver.find_element(*self.alias).send_keys(alias)

    def get_register_button(self, ):
        self._driver.find_element(*self.registerbutton).click()
        return Account(self)

    def get_account_error_message(self):
        return self._driver.find_element(*self.account_error_message)

    def create_account(self, user):
        self.get_mr()
        self.set_first_name(user.first_name)
        self.set_last_name(user.last_name)
        self.set_email(user.email)
        self.set_password(user.password)
        self.get_day(user.day)
        self.get_month(user.month)
        self.get_year(user.year)
        self.set_address(user.address)
        self.set_city(user.city)
        self.get_state(user.state)
        self.set_post_code(user.post_code)
        self.get_country(user.country)
        self.set_mobile_phone(user.mobile_phone)
        self.set_alias(user.alias)
        self.get_register_button()
        return Account(self)


