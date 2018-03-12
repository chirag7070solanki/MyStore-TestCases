from MyStore.Utilities import  log, MouseEvent
from MyStore.Utilities.ObjectRepo import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ele_myaccount(driver):
    # This methd gives element for MyAccount button
    # Locator comes from Object Repository
    try:
        print(*HomePage.My_Account)
        ele = driver.find_element(*HomePage.My_Account)
        log.info("My Account element is found")
        return ele
    except:
        log.error("My Account element not found")


def ele_logout(driver):
    # This method gives element "logout"
    # Locator comes from Object Repository
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(HomePage.logout))
        ele = driver.find_element(*HomePage.logout)
        log.info("Logout button found ")
        return ele
    except:
        log.error("Logout button NOT found ")


def login_name(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(HomePage.logout))
        ele = driver.find_element(*HomePage.login_name)
        log.info("Login Name Found")
        return ele
    except:
        log.error("Login Name NOT Found")


def product_type(driver, item):
    # This method is used to select a Product category
    # and then select product type (Accessories/iMacs/iPads/iPhones/iPods/Macbooks)
    boolval = MouseEvent.mouseevent(driver, item)
    return boolval

