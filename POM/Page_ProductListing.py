from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MyStore.Utilities import log
from MyStore.Utilities.ObjectRepo import ProductListing


def product1(driver):
    # This method return element for product 1
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(ProductListing.product_1))
        ele = driver.find_element(*ProductListing.product_1)
        log.info("product 1 is found")
        return ele
    except:
        log.info("product 1 is NOT found")

# I yet have to add methods for product 2 and so on......


def go_to_cart(driver):
    # This method return element for Go to cart button
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(ProductListing.go_to_cart))
        ele = driver.find_element(*ProductListing.go_to_cart)
        log.info("GoTo Cart button found")
        return ele
    except:
        log.info("GoTo Cart button NOT found")


def product_name_Add_to_cart(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(ProductListing.product_name_cart))
        ele = driver.find_element(*ProductListing.product_name_cart)
        log.info("Add to cart button found")
        return ele
    except:
        log.error("Add to cart button NOT found")


def alert(driver):
    boolval = False
    try:
        wait = WebDriverWait(driver, 10)
        # wait.until(EC.presence_of_element_located(ProductListing.alert))
        wait.until(EC.text_to_be_present_in_element(ProductListing.alert, "Item has been added to your cart!"))
        ele = driver.find_element(*ProductListing.alert)
        boolval = True
        log.info("Alert found")
    except:
        boolval = False
        log.info("Alert NOT found")
    return boolval


def ele_like(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(ProductListing.like))
        ele = driver.find_element(*ProductListing.like)
        log.info("like element found")
        return ele
    except:
        log.error("like element NOT found")


def name_product(driver, product):
    try:
        wait = WebDriverWait(driver, 10)
        if product == "Magic Mouse":
            wait.until(EC.presence_of_element_located(ProductListing.magic_mouse))
            ele = driver.find_element(*ProductListing.magic_mouse)
            log.info(product + " element found")
            return ele
        elif product == "Apple TV":
            wait.until(EC.presence_of_element_located(ProductListing.appleTV))
            ele = driver.find_element(*ProductListing.appleTV)
            log.info(product + " element found")
            return ele
        elif product == "Sennheiser RS 120":
            wait.until(EC.presence_of_element_located(ProductListing.Sennheiser))
            ele = driver.find_element(*ProductListing.Sennheiser)
            log.info(product + " element found")
            return ele
        elif product == "Skullcandy PLYR 1 – Black":
            wait.until(EC.presence_of_element_located(ProductListing.Skullcandy))
            ele = driver.find_element(*ProductListing.Skullcandy)
            log.info(product + " element found")
            return ele
        elif product == "Apple 27 inch Thunderbolt Display":
            wait.until(EC.presence_of_element_located(ProductListing.apple_display))
            ele = driver.find_element(*ProductListing.apple_display)
            log.info(product + " element found")
            return ele
        elif product == "Asus MX239H 23-inch Widescreen AH":
            wait.until(EC.presence_of_element_located(ProductListing.Asus))
            ele = driver.find_element(*ProductListing.Asus)
            log.info(product + " element found")
            return ele
        elif product == "Apple iPad 2 16GB, Wi-Fi, 9.7in – Black":
            wait.until(EC.presence_of_element_located(ProductListing.ipad2_16))
            ele = driver.find_element(*ProductListing.ipad2_16)
            log.info(product + " element found")
            return ele
        elif product == "Apple iPad 6 32GB (White, 3D)":
            wait.until(EC.presence_of_element_located(ProductListing.ipad_6_32))
            ele = driver.find_element(*ProductListing.ipad_6_32)
            log.info(product + " element found")
            return ele
        elif product == "Apple iPhone 4S 16GB SIM-Free – Black":
            wait.until(EC.presence_of_element_located(ProductListing.iphone_4s_16))
            ele = driver.find_element(*ProductListing.iphone_4s_16)
            log.info(product + " element found")
            return ele
        elif product == "Apple iPhone 4S 32GB SIM-Free – White":
            wait.until(EC.presence_of_element_located(ProductListing.iphone_4s_32))
            ele = driver.find_element(*ProductListing.iphone_4s_32)
            log.info(product + " element found")
            return ele
        elif product == "Apple iPod touch 32GB 5th Generation – Black":
            wait.until(EC.presence_of_element_located(ProductListing.ipod_32gb))
            ele = driver.find_element(*ProductListing.ipod_32gb)
            log.info(product + " element found")
            return ele
        elif product == "Apple iPod touch Large":
            wait.until(EC.presence_of_element_located(ProductListing.ipod_touch))
            ele = driver.find_element(*ProductListing.ipod_touch)
            log.info(product + " element found")
            return ele
        elif product == "Apple 13-inch MacBook Pro":
            wait.until(EC.presence_of_element_located(ProductListing.macbook))
            ele = driver.find_element(*ProductListing.macbook)
            log.info(product + " element found")
            return ele
    except:
        log.error(product + " element NOT found")
