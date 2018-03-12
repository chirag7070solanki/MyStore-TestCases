from MyStore.Utilities import log
from MyStore.POM import Page_CheckOut


def verify_name_and_price(driver):
    if Page_CheckOut.ele_product_name(driver).text == "Magic Mouse" and Page_CheckOut.ele_product_price(driver).text == "$150.00":
        log.info("Product name and price verification successful")
        return True
    else:
        log.info("Product name and price verification Unsuccessful")
        return False


def click_continue_button(driver):
    try:
        Page_CheckOut.ele_continue(driver).click()
        log.info("Continue button clicked")
        return True
    except:
        log.info("Continue button NOT clicked")
        return False


def click_remove_button(driver):
    try:
        Page_CheckOut.ele_remove(driver).click()
        log.info("Remove button clicked")
        return True
    except:
        log.info("Remove button NOT clicked")
        return False


def enter_text_in_quantity(driver):
    try:
        Page_CheckOut.ele_quantity(driver).send_keys("1")
        log.info("1" + " is added in quantity Textbox")
        return True
    except:
        log.info("User can NO add text in quantity Textbox")
        return False


def check_product_details(driver):
    retval = True
    if Page_CheckOut.ele_product_name(driver).text == "Magic Mouse":
        log.info("Product name verification successful")
    else:
        retval = False
        log.info("Product name verification failed")

    if Page_CheckOut.ele_product_price(driver).text == "$150.00":
        log.info("Product price verification successful")
    else:
        retval = False
        log.info("Product price verification failed")

    # If verification is successful go ahead with clicking continue button

    if retval:
        Page_CheckOut.ele_continue(driver).click()
        log.info("Continue button clicked")

