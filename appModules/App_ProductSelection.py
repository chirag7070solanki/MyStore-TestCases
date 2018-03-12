from MyStore.Utilities import Excel, log, constants
from MyStore.POM import Page_HomePage, Page_ProductListing


def select_a_product(excel_obj, driver, itestcaserow):
    # This module takes which type of product to select from TestData sheet
    # and select that product
    type_product = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_product_name)
    Page_HomePage.product_type(driver, type_product)


def select_a_product_name(driver, excel_obj, itestcaserow):
    product = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_product_no)
    product_list = product.split(",")
    log.info(product_list)
    return_list = []
    for pr in product_list:
        try:
            Page_ProductListing.name_product(driver, pr).click()
            log.info(pr + " clicked")
            driver.back()
            return_list.append(True)
        except:
            log.error(pr + " NOT clicked")
            return_list.append(False)
    return return_list


def select_a_single_product_name(driver, excel_obj, itestcaserow):
    product = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_product_no)
    try:
        Page_ProductListing.name_product(driver, product).click()
        log.info(product + " clicked")
        return True
    except:
        log.error(product + " NOT clicked")
        return False


def click_like(driver):
    try:
        Page_ProductListing.ele_like(driver).click()
        log.info("like button clicked")
        return True
    except:
        log.error("like button NOT clicked")
        return False


def click_product_name_Add_to_cart(driver):
    try:
        Page_ProductListing.product_name_Add_to_cart(driver).click()
        log.info("Add to cart button clicked")
        return True
    except:
        log.error("Add to cart button NOT clicked")
        return False


def test_for_sub_category(driver, type):
    ret_val = Page_HomePage.product_type(driver, type)
    page_title = type + " | ONLINE STORE"
    if driver.title == page_title and ret_val:
        return True
    else:
        return False


def selecting_product_1(driver):
    ret_val = True
    try:
        Page_ProductListing.product1(driver).click()
        log.info("product 1 is added to cart")
    except:
        ret_val = False
        log.info("product 1 is NOT added to cart")
    return ret_val


def check_for_alert(driver):
    if Page_ProductListing.alert(driver):
        return True
    else:
        return False


def click_on_go_to_cart_button(driver):
    ret_val = True
    try:
        Page_ProductListing.go_to_cart(driver).click()
        log.info("GoTo Cart button clicked")
    except:
        ret_val = False
        log.error("GoTo Cart button NOT clicked")
    return ret_val


def select_a_product_no(excel_obj, driver, itestcaserow):
    # This module takes which number of product to select from TestData sheet
    # and select that product
    product_no = Excel.Excel.get_content(excel_obj, row=itestcaserow, clm=constants.col_product_no)

    # I yet have to add other numbers of product (product 2/ none etc...)
    ret_val = True
    if product_no == "Product 1":
        try:
            Page_ProductListing.product1(driver).click()
            log.info("product 1 is added to cart")
        except:
            ret_val = False
            log.info("product 1 is NOT added to cart")
    # click_on_go_to_cart_button(driver)
    # Page_ProductListing.go_to_cart(driver).click()
    # log.info("GoTo Cart button clicked")
    return  ret_val
