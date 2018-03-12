from MyStore.Utilities import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MyStore.Utilities.ObjectRepo import CustomerDetails


def ele_go_back(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(CustomerDetails.go_back))
        ele = driver.find_element(*CustomerDetails.go_back)
        log.info("Go Back button element found")
        return ele
    except:
        log.error("Go Back button element NOT found")


def ele_email(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(CustomerDetails.email_txt))
        ele = driver.find_element(*CustomerDetails.email_txt)
        log.info("Email element found")
        return ele
    except:
        log.info("Email element NOT found")


def give_firstname(driver):
    # Give element for first name field
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(CustomerDetails.firstname_txt))
        ele = driver.find_element(*CustomerDetails.firstname_txt)
        log.info('FirstName field found')
        return ele
    except:
        log.info('FirstName field not found')


def give_lastname(driver):
    # Give element for last name field
    try:
        ele = driver.find_element(*CustomerDetails.lastname_txt)
        log.info('LastName field found')
        return ele
    except:
        log.info('LastName field not found')


def give_address(driver):
    # Give element for Address field
    try:
        ele = driver.find_element(*CustomerDetails.address_txt)
        log.info('Address field found')
        return ele
    except:
        log.info('Address field not found')


def give_city(driver):
    # Give element for city field
    try:
        ele = driver.find_element(*CustomerDetails.city_txt)
        log.info('City field found')
        return ele
    except:
        log.info('City field not found')


def give_country(driver):
    # Give element for country field
    try:
        ele = driver.find_element(*CustomerDetails.country_ddl)
        log.info('Country field found')
        return ele
    except:
        log.info('Country field not found')


def give_phone(driver):
    # Give element for phone number field
    try:
        ele = driver.find_element(*CustomerDetails.phone_txt)
        log.info('Phone number field found')
        return ele
    except:
        log.info('Phone number field not found')


def give_checkbox_ship(driver):
    # Give check box for shipping address is same as permanent address
    try:
        ele = driver.find_element(*CustomerDetails.shipping_address_checkbox)
        log.info('Shipping address checkbox found')
        return ele
    except:
        log.info('Shipping address checkbox NOT found')


def give_btn_purchase(driver):
    # Get element for Purchase Button
    try:
        ele = driver.find_element(*CustomerDetails.purchase_button)
        log.info('Purchase found')
        return ele
    except:
        log.info('Purchase NOT found')
