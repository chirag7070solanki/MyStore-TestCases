from selenium.webdriver.common.action_chains import ActionChains
from MyStore.Utilities import log
from MyStore.Utilities.ObjectRepo import ProductListing, HomePage


def mouseevent(driver, item):
    boolval = False
    ele = driver.find_element(*HomePage.product_category)
    act = ActionChains(driver).move_to_element(ele)
    act.perform()
    log.info("Product Category is clicked")
    try:
        if item == "Accessories":
            ele = driver.find_element(*HomePage.product_accessories)
            act.move_to_element(ele).click().perform()
            log.info(item + " element is clickable")
        if item == "iMacs":
            ele = driver.find_element(*HomePage.product_iMacs)
            act.move_to_element(ele).click().perform()
        if item == "iPads":
            ele = driver.find_element(*HomePage.product_iPads)
            act.move_to_element(ele).click().perform()
        if item == "iPhones":
            ele = driver.find_element(*HomePage.product_iPhones)
            act.move_to_element(ele).click().perform()
        if item == "iPods":
            ele = driver.find_element(*HomePage.product_iPods)
            act.move_to_element(ele).click().perform()
        if item == "MacBooks":
            ele = driver.find_element(*HomePage.product_MacBooks)
            act.move_to_element(ele).click().perform()
        boolval = True
        log.info(item + " is clickable")
    except:
        boolval = False
        log.info(item + " is NOT clickable")
    return boolval

