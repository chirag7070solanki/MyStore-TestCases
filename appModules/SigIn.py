from MyStore.POM import Page_HomePage, Page_LogIn
from MyStore.Utilities.Excel import Excel, log
from MyStore.Utilities import constants


def click_my_account_button(driver):
    ret_val = True
    try:
        Page_HomePage.ele_myaccount(driver).click()
        log.info("My Account Button is clicked")
    except:
        log.info("My Account Button is NOT clicked")
        ret_val = False
    return ret_val


def enter_text_in_user_id_textbox(driver, excel_obj, itestcaserow):
    ret_val = True
    try:
        user_name = Excel.get_content(excel_obj, itestcaserow, constants.col_user_name)
        Page_LogIn.ele_user_name(driver).send_keys(user_name)
        log.info(user_name + " is entered")
    except:
        ret_val = False
    return ret_val


def enter_text_in_password_textbox(driver, excel_obj, itestcaserow):
    ret_val = True
    try:
        password = Excel.get_content(excel_obj, itestcaserow, constants.col_password)
        Page_LogIn.ele_password(driver).send_keys(password)
        log.info(password + " is entered")
    except:
        ret_val = False
    return ret_val


def click_login_button(driver):
    ret_val = True
    try:
        Page_LogIn.ele_login_button(driver).click()
        log.info("Login Button is clicked")
    except:
        ret_val = False
    return ret_val


def check_for_successful_login(driver, excel_obj, itestcaserow):
    ret_val = True
    user_name = Excel.get_content(excel_obj, itestcaserow, constants.col_user_name)
    try:
        if Page_HomePage.login_name(driver).text == user_name:
            log.info("Login is successful")
        else:
            log.info("Login is successful")
            ret_val = False
    except:
        ret_val = False
    return ret_val


def no_username_and_password(driver):
    try:
        if Page_LogIn.ele_error1(driver).text == "Please enter your username and password.":
            log.info("error found")
            return True
        else:
            log.error("error not found")
            return False
    except:
        return False


def no_password(driver):
    try:
        if Page_LogIn.ele_error2(driver).text == "ERROR: The password field is empty.":
            log.info("error found")
            return True

        else:
            log.error("error not found")
            return False
    except:
        return False


def no_user_id(driver):
    try:
        if Page_LogIn.ele_error3(driver).text == "ERROR: The username field is empty.":
            log.info("error found")
            return True
        else:
            log.error("error not found")
            return False
    except:
        return False


def wrong_login(driver):
    try:
        if Page_LogIn.ele_error4(driver).text == "ERROR: The password you entered for the username chirag_test is incorrect. Lost your password?":
            log.info("error found")
            return True
        else:
            log.error("error not found")
            return False
    except:
        return False


def check_for_logout_button(driver):
    Page_HomePage.ele_logout(driver)


def click_lost_password(driver):
    try:
        Page_LogIn.ele_lost_password(driver).click()
        log.info("Lost Password button clicked")
        return True
    except:
        log.error("Lost Password button NOT clicked")
        return False


def click_remember_me(driver):
    try:
        Page_LogIn.ele_remember_me(driver).click()
        log.info("Remember me checkbox clicked")
        return True
    except:
        log.error("Remember me checkbox NOT clicked")
        return False


def attempsignin(excel_obj, driver, itestcaserow):

    # Clicking on MyAccount button on Home Page of an application
    Page_HomePage.ele_myaccount(driver).click()

    # Give user name and password input on LogIn Page
    user_name = Excel.get_content(excel_obj, itestcaserow, constants.col_user_name)
    Page_LogIn.ele_user_name(driver).send_keys(user_name)
    log.info(user_name + " is added")
    password = Excel.get_content(excel_obj, itestcaserow, constants.col_password)
    Page_LogIn.ele_password(driver).send_keys(password)
    log.info("Password is added")

    # Clicking on Login Button on LogIn Page
    Page_LogIn.ele_login_button(driver).click()
    log.info("LogIn button is clicked")

    # Upon successful login, Logout button is visible
    # To verify this, we are checking for logout button's presence
    Page_HomePage.ele_logout(driver)
