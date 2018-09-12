from selenium.webdriver.common.by import By


class Locator:

#home page locator
    contactus = (By.XPATH, "//div[@id='contact-link']")
    singin = (By.XPATH, "//div[@class='header_user_info']")
    women = (By.XPATH, "//*[contains(text(), 'Women')]")
    search = (By.ID, "search_query_top")
    buttonsearch = (By.NAME, "submit_search")



#registration page locator
    emailadress = (By.ID, "email_create")
    createanaccount = (By.ID, "SubmitCreate")
    mr = (By.ID, "id_gender1")
    firstname = (By.ID, "customer_firstname")
    lastname = (By.ID, "customer_lastname")
    email = (By.ID, "email")
    password = (By.ID, "passwd")
    day = (By.ID, "days")
    month = (By.ID, "months")
    year = (By.ID, "years")
    address = (By.ID, "address1")
    city = (By.ID, "city")
    state = (By.ID, "id_state")
    postcode = (By.ID, "postcode")
    country = (By.ID, "id_country")
    mobilephone = (By.ID, "phone_mobile")
    alias = (By.ID, "alias")
    registerbutton = (By.ID, "submitAccount")

#my account page locator
    myaccount = (By.XPATH, "//span[text()='My account']")
    mywishlists = (By.XPATH, "//span[text()='My wishlists']")

#product page locator
    topsellers = (By.XPATH, "//a[contains(.,'Top sellers')]")
    productcontainer = (By.XPATH, "//div[@class='product-container']")

#page ordered locator
    price = (By.ID, "our_price_display")
    quantity = (By.ID, "quantity_wanted")
    size = (By.ID, "group_1")
    addtocart = (By.ID, "add_to_cart")
    proceedtocheckout = (By.XPATH, "//a[contains(@class, 'btn btn-default button button-medium')]")
    totalprice = (By.ID, "total_price")




# for maintainability we can seperate web objects by page name

