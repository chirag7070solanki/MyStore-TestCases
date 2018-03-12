from MyStore.Utilities import log
from MyStore.Utilities.ObjectRepo import LogIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ele_user_name(driver):
    # This method gives element "user_name" (TextBox)
    # Locator comes from Object Repository
    try:
        ele = driver.find_element(*LogIn.user_text)
        log.info("User name TextBox found")
        return ele
    except:
        log.error("User name TextBox NOT found")


def ele_password(driver):
    # This method gives element "password"(TextBox)
    # Locator comes from Object Repository
    try:
        ele = driver.find_element(*LogIn.pwd_text)
        log.info("Password TextBox found")
        return ele
    except:
        log.error("Password TextBox NOT found")


def ele_login_button(driver):
    # This method gives element "login" (Button)
    # Locator comes from Object Repository
    try:
        ele = driver.find_element(*LogIn.login_button)
        log.info("Login button found")
        return ele
    except:
        log.error("Login button NOT found")


def ele_error1(driver):
    # error 1 = Please enter your username and password.
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element(LogIn.body, "Please enter your username and password."))
        ele = driver.find_element(*LogIn.body)
        log.info("error element found")
        return ele
    except:
        log.error("error element NOT found")


def ele_error2(driver):
    # error 2 = ERROR: The password field is empty.
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element(LogIn.body, "ERROR: The password field is empty."))
        ele = driver.find_element(*LogIn.body)
        log.info("error element found")
        return ele
    except:
        log.error("error element NOT found")


def ele_error3(driver):
    # error 3 = ERROR: The username field is empty.
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element(LogIn.body, "ERROR: The username field is empty."))
        ele = driver.find_element(*LogIn.body)
        log.info("error element found")
        return ele
    except:
        log.error("error element NOT found")


def ele_error4(driver):
    # error 4 = ERROR: The password you entered for the username chirag_test is incorrect.
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element(LogIn.body, "ERROR: The password you entered for the username chirag_test is incorrect. Lost your password?"))
        ele = driver.find_element(*LogIn.body)
        log.info("error element found")
        return ele
    except:
        log.error("error element NOT found")


def ele_lost_password(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(LogIn.lost_pwd))
        ele = driver.find_element(*LogIn.lost_pwd)
        log.info("Lost password element found")
        return ele
    except:
        log.error("Lost password element NOT found")


def ele_remember_me(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(LogIn.remember))
        ele =  driver.find_element(*LogIn.remember)
        log.info("Remember me checkbox element found")
        return ele
    except:
        log.error("Remember me checkbox element NOT found")

