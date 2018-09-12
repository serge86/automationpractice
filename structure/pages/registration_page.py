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

    def getinformation(self):
        return self._driver.find_element(*self.information)

    def getmr(self):
        self._driver.find_element(*self.mr).click()
    
    def is_mr_radio_button_selected(self, element):
        return self._driver.find_element(*self.mr, element)

    def getmrs(self):
        return self._driver.find_element(*self.mrs)

    def setfirstname(self, Name):
        self._driver.find_element(*self.firstname).click()
        self._driver.find_element(*self.firstname).clear()
        self._driver.find_element(*self.firstname).send_keys(Name)

    def setlastname(self, Name):
        self._driver.find_element(*self.lastname).click()
        self._driver.find_element(*self.lastname).clear()
        self._driver.find_element(*self.lastname).send_keys(Name)

    def setemail(self, email):
        self._driver.find_element(*self.email).click()
        self._driver.find_element(*self.email).clear()
        self._driver.find_element(*self.email).send_keys(email)

    def setpassword(self, password):
        self._driver.find_element(*self.password).click()
        self._driver.find_element(*self.password).clear()
        self._driver.find_element(*self.password).send_keys(password)

    def getday(self, value):
        select_day = Select(self._driver.find_element_by_id("days"))
        select_day.select_by_value(value)        

    def getmonth(self, value):
        select_month = Select(self._driver.find_element_by_id("months"))
        select_month.select_by_value(value)        

    def getyear(self, value):
        select_year = Select(self._driver.find_element_by_id("years"))
        select_year.select_by_value(value)    

    def setaddress(self, address):
        self._driver.find_element(*self.address).clear()
        self._driver.find_element(*self.address).send_keys(address)

    def setcity(self, city):
        self._driver.find_element(*self.city).clear()
        self._driver.find_element(*self.city).send_keys(city)
      
    
    def getstate(self, value):
        select_st = Select(self._driver.find_element_by_id("id_state"))
        select_st.select_by_value(value)
        #select_st.select_by_index(self, index)
        #select_st.select_by_visible_text(self, "Colorado")
        #self.country.click()
        
    # def select_state(self, state):
    #     self._driver.find_element_by_id("id_state").click()
    #     select_st = Select(self._driver.find_element_by_id("id_state"))
    #     select_st.select_by_value(self)
        
        
    # def choise_state(self):
    #     Select state = Select(self._driver.findElement(By.id("id_state")));
    #     state.selectByVisibleText("Banana");
    #     state.selectByIndex(1);
        
        
    def setpostcode(self, postcode):
        self._driver.find_element(*self.postcode).clear()
        self._driver.find_element(*self.postcode).send_keys(postcode)

    def getcountry(self, text):
        select_cou = Select(self._driver.find_element_by_id("id_country"))
        select_cou.select_by_visible_text(text)

    def setmobilephone(self, mobilephone):
        self._driver.find_element(*self.mobilephone).clear()
        self._driver.find_element(*self.mobilephone).send_keys(mobilephone)

    def setalias(self, email):
        self._driver.find_element(*self.alias).clear()
        self._driver.find_element(*self.alias).send_keys(email)
        

    def getregisterbutton(self,):
        self._driver.find_element(*self.registerbutton).click()
        return Account(self)

    def getaccount_error_message(self):
        return self._driver.find_element(*self.account_error_message)

    #def create_account(self):

