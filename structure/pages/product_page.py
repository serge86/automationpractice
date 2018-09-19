from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Product:
    url = "http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=woman&submit_search="

    def __init__(self, driver):
        self._driver = driver

# product_page element
        self.sortby = (By.XPATH, "//div[@class='select selector1']")

    def get_url(self, url):
        return self._driver.get_url(url)

    def get_sort_by(self):
        return self._driver.find_element(*self.sortby)



