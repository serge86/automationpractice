"""
Tests
"""
from structure.pages.home_page import driver
from structure.test_utility.conftest import home, product, preregister, account, register, user, url


def test_check_search():
    """
    Test that verify a search of product

    :return: label of this product must be displayed
    """
    home.set_search("woman")
    product.get_sort_by()
    assert product.get_sort_by().is_displayed()


def test_invalid_email():
    """
    Test that verify a possibility to enter invalid email
    :return: error message
    """
    home.get_sing_in()
    preregister.set_email_adress("hello")
    assert preregister.get_error_message().is_enabled()


def test_preregistration():
    """
    Test check a message and verify url
    :return: True
    """
    home.get_sing_in()
    preregister.set_email_adress("778@gmail.com")
    assert register.get_information().is_enabled()
    assert driver.current_url, register.get_url(url)


def test_create_account():
    """
    Create account
    :return: my account page
    """
    driver.get("http://automationpractice.com/index.php?controller=\n"
               "authentication&back=my-account#account-creation")
    preregister.set_email_adress("800@gmail.com")
    register.get_mr()
    register.set_first_name("Vano")
    register.set_last_name("Petrov")
    register.set_email("555@gmail.com")
    register.set_password("98765")
    register.get_day("7")
    register.get_month("11")
    register.get_year("1955")
    register.set_address("MMM")
    register.set_city("London")
    register.get_state("6")
    register.set_post_code("54321")
    register.get_country("United States")
    register.set_mobile_phone("256897412")
    register.set_alias("555@gmail.com")
    register.get_register_button()
    assert account.get_my_account().is_displayed


def test_create_existing_account():
    """
    Test that verify a creation in existing account
    :return: error message is enabled
    """
    driver.get("http://automationpractice.com/index.php?controller=\n"
               "authentication&back=my-account#account-creation")
    preregister.set_email_adress("778@gmail.com")
    register.get_mr()
    register.set_first_name("Ivan")
    register.set_last_name("Popov")
    register.set_email("444@gmail.com")
    register.set_password("12345")
    register.get_day("8")
    register.get_month("12")
    register.get_year("1905")
    register.set_address("AAAA")
    register.set_city("Lviv")
    register.get_state("6")
    register.set_post_code("56789")
    register.get_country("United States")
    register.set_mobile_phone("123456789")
    register.set_alias("444@gmail.com")
    register.get_register_button()
    assert register.get_account_error_message().is_enabled()


def test_create_new_account():
    """
    Test verify a creation an account
    :return: my account page
    """
    driver.get("http://automationpractice.com/index.php?controller=\n"
               "authentication&back=my-account#account-creation")
    preregister.set_email_adress("778@gmail.com")
    register.create_account(user)
    assert account.get_my_account().is_displayed
