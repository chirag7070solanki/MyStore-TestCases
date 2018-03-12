from MyStore.Utilities import log, Excel, constants
from MyStore.POM import Page_CustomerDetails
from selenium.webdriver.support.ui import Select


def enter_in_email_txtbox(driver, excel_obj,itestcaserow):
    email = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_email)
    try:
        ele = Page_CustomerDetails.ele_email(driver)
        ele.clear()
        ele.send_keys(email)
        log.info(email + " is entered")
        return True
    except:
        log.info(email + " is NOT entered")
        return False


def enter_in_firstname_txtbox(driver, excel_obj,itestcaserow):
    firstname = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_fname)
    try:
        ele = Page_CustomerDetails.give_firstname(driver)
        ele.clear()
        ele.send_keys(firstname)
        log.info(firstname + " is entered")
        return True
    except:
        log.info(firstname + " is NOT entered")
        return False


def enter_in_lastname_txtbox(driver, excel_obj,itestcaserow):
    lastname = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_lname)
    try:
        ele = Page_CustomerDetails.give_lastname(driver)
        ele.clear()
        ele.send_keys(lastname)
        log.info(lastname + " is entered")
        return True
    except:
        log.info(lastname + " is NOT entered")
        return False


def enter_in_address_txtbox(driver, excel_obj,itestcaserow):
    address = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_add)
    try:
        ele = Page_CustomerDetails.give_address(driver)
        ele.clear()
        ele.send_keys(address)
        log.info(address + " is entered")
        return True
    except:
        log.info(address + " is NOT entered")
        return False


def enter_in_city_txtbox(driver, excel_obj,itestcaserow):
    city = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_city)
    try:
        ele = Page_CustomerDetails.give_city(driver)
        ele.clear()
        ele.send_keys(city)
        log.info(city + " is entered")
        return True
    except:
        log.info(city + " is NOT entered")
        return False


def select_country(driver, excel_obj,itestcaserow):
    country = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_country)
    ele = Page_CustomerDetails.give_country(driver)
    sel = Select(ele)
    sel.select_by_visible_text(country)
    try:
        ele = Page_CustomerDetails.give_country(driver)
        sel = Select(ele)
        sel.select_by_visible_text(country)
        log.info(country + " is entered")
        return True
    except:
        log.info(country + " is NOT entered")
        return False


def enter_in_phone_txtbox(driver, excel_obj,itestcaserow):
    phone = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_phone)
    try:
        ele = Page_CustomerDetails.give_phone(driver)
        ele.clear()
        ele.send_keys(phone)
        log.info(phone + " is entered")
        return True
    except:
        log.info(phone + " is NOT entered")
        return False


def click_shipping_checkbox(driver):
    
    try:
        Page_CustomerDetails.give_checkbox_ship(driver).click()
        log.info("Checkbox checked")
        return True
    except:
        log.info("Checkbox NOT checked")
        return False


def click_purchase_button(driver):
    try:
        Page_CustomerDetails.give_btn_purchase(driver).click()
        log.info("Purchase button clicked")
        return True
    except:
        log.info("Purchase button NOT clicked")
        return False


def click_go_back_button(driver):
    try:
        Page_CustomerDetails.ele_go_back(driver).click()
        log.info("Go Back button clicked")
        return True
    except:
        log.error("Go Back buttton NOT clicked")
        return False


def customer_details(excel_obj, driver, itestcaserow):

    # This method enters all details (email, firstname, lastname, city,
    # country, address, phone number etc...) on checkout page
    # All these data comes from TesData sheet

    email = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_email)
    ele = Page_CustomerDetails.ele_email(driver)
    ele.clear()
    ele.send_keys(email)
    log.info(email + " is entered")

    firstname = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_fname)
    ele = Page_CustomerDetails.give_firstname(driver)
    ele.clear()
    ele.send_keys(firstname)
    log.info(firstname + " is entered")

    lastname = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_lname)
    ele = Page_CustomerDetails.give_lastname(driver)
    ele.clear()
    ele.send_keys(lastname)
    log.info(lastname + " is entered")

    Page_CustomerDetails.give_checkbox_ship(driver).click()
    log.info("Checkbox checked")

    address = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_add)
    ele = Page_CustomerDetails.give_address(driver)
    ele.clear()
    ele.send_keys(address)
    log.info(address + " is entered")

    city = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_city)
    ele = Page_CustomerDetails.give_city(driver)
    ele.clear()
    ele.send_keys(city)
    log.info(city + " is entered")

    country = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_country)
    ele = Page_CustomerDetails.give_country(driver)
    sel = Select(ele)
    sel.select_by_visible_text(country)

    phone = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_phone)
    ele = Page_CustomerDetails.give_phone(driver)
    ele.clear()
    ele.send_keys(phone)
    log.info(phone + " is entered")

    Page_CustomerDetails.give_btn_purchase(driver).click()
    log.info("Purchase button clicked")

