from MyStore.Utilities import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MyStore.Utilities.ObjectRepo import Checkout


def ele_product_name(driver):
    # This method return element of product name
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(Checkout.product_name))
        ele = driver.find_element(*Checkout.product_name)
        log.info("Prodcut name element found")
        return ele
    except:
        log.error("Prodcut name element NOT found")


def ele_product_price(driver):
    # This method return element of product price
    try:
        ele = driver.find_element(*Checkout.product_price)
        log.info("Prodcut price element found")
        return ele
    except:
        log.error("Prodcut price element NOT found")


def ele_remove(driver):
    try:
        ele = driver.find_element(*Checkout.remove_button)
        log.info("Remove button found")
        return ele
    except:
        log.info("Remove button NOT found")


def ele_quantity(driver):
    try:
        ele = driver.find_element(*Checkout.quantity)
        log.info("Quantity element found")
        return ele
    except:
        log.info("Quantity element NOT found")


def ele_continue(driver):
    # This method return element of continue button
    try:
        ele = driver.find_element(*Checkout.continue_button)
        log.info("Continue button found")
        return ele
    except:
        log.info("Continue button NOT found")