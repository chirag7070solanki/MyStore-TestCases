from selenium.webdriver.common.by import By


class HomePage(object):
    My_Account = (By.XPATH, ".//*[@id='account']/a")
    logout = (By.XPATH, "//*[@id='account_logout']/a")
    product_category = (By.LINK_TEXT, "Product Category")
    product_accessories = (By.LINK_TEXT, "Accessories")
    product_iMacs = (By.LINK_TEXT, "iMacs")
    product_iPads = (By.LINK_TEXT, "iPads")
    product_iPhones = (By.LINK_TEXT, "iPhones")
    product_iPods = (By.LINK_TEXT, "iPods")
    product_MacBooks = (By.LINK_TEXT, "MacBooks")
    login_name = (By.XPATH, ".//*[@id='wp-admin-bar-my-account']/a/span")


class ProductListing(object):
    product_1 = (By.XPATH, ".//*[@id='default_products_page_container']/div[3]/div[2]/form/div[2]/div[1]/span/input")
    product_name_cart = (By.XPATH,  ".//*[@id='single_product_page_container']/div[1]/div[2]/form/div[2]/div[1]/span/input")
    go_to_cart = (By.XPATH, "/html/body/div[2]/div/div/header/div[2]/a/span[1]")
    alert = (By.XPATH, ".//*[@id='default_products_page_container']/div[3]/div[2]/form/div[2]/div[1]/div[2]")
    magic_mouse = (By.LINK_TEXT, "Magic Mouse")
    macbook = (By.LINK_TEXT, "Apple 13-inch MacBook Pro")
    ipod_32gb = (By.LINK_TEXT, "Apple iPod touch 32GB 5th Generation – Black")
    ipod_touch = (By.LINK_TEXT, "Apple iPod touch Large")
    iphone_4s_16 = (By.LINK_TEXT, "Apple iPhone 4S 16GB SIM-Free – Black")
    iphone_4s_32 = (By.LINK_TEXT, "Apple iPhone 4S 32GB SIM-Free – White")
    ipad2_16 = (By.LINK_TEXT, "Apple iPad 2 16GB, Wi-Fi, 9.7in – Black")
    ipad_6_32 = (By.LINK_TEXT, "Apple iPad 6 32GB (White, 3D)")
    appleTV = (By.LINK_TEXT, "Apple TV")
    Sennheiser = (By.LINK_TEXT, "Sennheiser RS 120")
    Skullcandy = (By.LINK_TEXT, "Skullcandy PLYR 1 – Black")
    apple_display = (By.LINK_TEXT, "Apple 27 inch Thunderbolt Display")
    Asus = (By.LINK_TEXT, "Asus MX239H 23-inch Widescreen AH")
    like = (By.XPATH, ".//*[@id='u_0_2']")

class Checkout(object):
    product_name = (By.XPATH, ".//*[@id='checkout_page_container']/div[1]/table/tbody/tr[2]/td[2]/a")
    product_price = (By.XPATH, ".//*[@id='checkout_page_container']/div[1]/table/tbody/tr[2]/td[4]/span")
    continue_button = (By.XPATH, ".//*[@id='checkout_page_container']/div[1]/a/span")
    remove_button = (By.XPATH, ".//*[@id='checkout_page_container']/div[1]/table/tbody/tr[2]/td[6]/form/input[4]")
    quantity = (By.XPATH, "//*[@id='checkout_page_container']/div[1]/table/tbody/tr[2]/td[3]/form/input[1]")


class CustomerDetails(object):
    email_txt = (By.XPATH, ".//*[@id='wpsc_checkout_form_9']")
    firstname_txt = (By.XPATH, ".//*[@id='wpsc_checkout_form_2']")
    lastname_txt = (By.XPATH, ".//*[@id='wpsc_checkout_form_3']")
    address_txt = (By.XPATH, ".//*[@id='wpsc_checkout_form_4']")
    city_txt = (By.XPATH, ".//*[@id='wpsc_checkout_form_5']")
    country_ddl = (By.XPATH, ".//*[@id='wpsc_checkout_form_7']")
    phone_txt = (By.XPATH, ".//*[@id='wpsc_checkout_form_18']")
    shipping_address_checkbox = (By.XPATH, "//*[@id='shippingSameBilling']")
    purchase_button = (By.XPATH, ".//*[@id='wpsc_shopping_cart_container']/form/div[4]/div/div/span/input")
    go_back = (By.XPATH, ".//*[@id='wpsc_shopping_cart_container']/form/a/span")


class LogIn(object):
    user_text = (By.XPATH, "//input[@id='log']")
    pwd_text = (By.XPATH, "//input[@id='pwd']")
    login_button = (By.XPATH, "//input[@id='login']")
    body = (By.XPATH, ".//*[@id='ajax_loginform']/p[1]")
    lost_pwd = (By.XPATH, ".//*[@id='ajax_loginform']/p[1]/a")
    remember = (By.ID, "rememberme")

