import pytest, unittest
from MyStore.Utilities import utils, Excel, log
from MyStore.appModules import SigIn, App_ProductSelection, App_VerifyPurchase, App_CustomerDetails
import time


class Test_TC001:

    def setup_class(self):
        self.excel_obj = Excel.Excel()
        self.excel_obj.setexcelfile()
        self.itestcaserow = Excel.Excel.get_row_num(self.excel_obj, "Test2")

    def setup_method(self):
        log.starttestcase()
        self.driver = utils.openbrowser(self.excel_obj, self.itestcaserow)

    def test_tc001(self):
        if SigIn.click_my_account_button(self.driver):
            log.info("My Account element is clickable - TC001 is PASSED")
        else:
            log.error("Element is not clickable - TC001 is FAILED")

    def test_tc002(self):
        SigIn.click_my_account_button(self.driver)
        if SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("User ID TextBox is taking texts - TC002 is PASSED")
        else:
            log.error("User ID TextBox is not taking texts - TC002 is FAILED")

    def test_tc002b(self):
        SigIn.click_my_account_button(self.driver)
        if SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("Password TextBox is taking texts -- TC002 is PASSED")
        else:
            log.error("Password TextBox is not taking texts - TC002 is FAILED")

    def test_tc003(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)

        if SigIn.click_login_button(self.driver) and SigIn.check_for_successful_login(self.driver, self.excel_obj,self.itestcaserow):
            log.info("LogIn button is clickable - TC003 is PASSED")
        else:
            log.error("LogIn button is NOT clickable - TC003 is FAILED")

    # def test_tc004(self):
    #
    #     SigIn.click_my_account_button(self.driver)
    #     SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
    #     SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
    #     SigIn.click_login_button(self.driver)
    #
    #     if SigIn.check_for_successful_login(self.driver, self.excel_obj,self.itestcaserow):
    #         log.info("LogIn Successful - TC004 is PASSED")
    #     else:
    #         log.info("LogIn Unsuccessful - TC004 is FAILED")

    def test_tc004(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.click_login_button(self.driver)
        if SigIn.no_username_and_password(self.driver):
            log.info("TC004 is PASSED")
        else:
            log.error("TC004 is FAILED")

    def test_tc005a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)

        if SigIn.no_password(self.driver):
            log.info("TC005 is PASSED")
        else:
            log.error("TC005 is FAILED")

    def test_tc006a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)

        if SigIn.no_user_id(self.driver):
            log.info("TC006 is PASSED")
        else:
            log.error("TC006 is FAILED")

    def test_tc009a(self):
        SigIn.click_my_account_button(self.driver)
        if SigIn.click_remember_me(self.driver):
            log.info("TC009 is PASSED")
        else:
            log.error("TC009 is FAILED")

    def test_tc010a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        if App_ProductSelection.test_for_sub_category(self.driver, "Accessories"):
            log.info("TC010 is PASSED")
        else:
            log.error("TC010 is FAILED")

    def test_tc011a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        if App_ProductSelection.test_for_sub_category(self.driver, "iMacs"):
            log.info("TC011 is PASSED")
        else:
            log.error("TC011 is FAILED")

    def test_tc012a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        if App_ProductSelection.test_for_sub_category(self.driver, "iPads"):
            log.info("TC012 is PASSED")
        else:
            log.error("TC012 is FAILED")

    def test_tc013a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        if App_ProductSelection.test_for_sub_category(self.driver, "iPhones"):
            log.info("TC013 is PASSED")
        else:
            log.error("TC013 is FAILED")

    def test_tc014a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        if App_ProductSelection.test_for_sub_category(self.driver, "iPods"):
            log.info("TC014 is PASSED")
        else:
            log.error("TC014 is FAILED")

    def test_tc015a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        if App_ProductSelection.test_for_sub_category(self.driver, "MacBooks"):
            log.info("TC015 is PASSED")
        else:
            log.error("TC015 is FAILED")

    def test_tc016a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)

        if App_ProductSelection.selecting_product_1(self.driver) and App_ProductSelection.check_for_alert(self.driver):
            log.info("Add to cart button is clickable and Alert available - TC016 is PASSED")
        else:
            log.error("Add to cart button is NOT clickable or Alert NOT available - TC016 is FAILED")

    def test_tc021a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)

        if App_ProductSelection.click_on_go_to_cart_button(self.driver):
            log.info("Go to cart button is clickable - TC013 is PASSED")
        else:
            log.error("Go to cart button is NOT clickable - TC013 is Failed")

    def test_tc022a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        if App_VerifyPurchase.verify_name_and_price(self.driver):
            log.info("Product name and price verification successful - TC014 is PASSED")
        else:
            log.error("Product name and price verification Unsuccessful - TC014 is FAILED")

    def test_tc023a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        if App_VerifyPurchase.click_remove_button(self.driver):
            log.info("User can click on Remove button - TC015 is PASSED")
        else:
            log.error("User can NOT click on Remove button - TC015 is FAILED")

    def test_tc024a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)

        if App_VerifyPurchase.enter_text_in_quantity(self.driver):
            log.info("User can add texts in Quantity TextBox - TC016 is PASSED")
        else:
            log.info("User can NOT add texts in Quantity TextBox - TC016 is PASSED")

    def test_tc025a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)

        if App_VerifyPurchase.click_continue_button(self.driver):
            log.info("Continue button is clickable - TC017 is PASSED")
        else:
            log.error("Continue button is NOT clickable - 7 is FAILED")
##############################################################################

    def test_tc026a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        if App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("User can add texts in email TextBox - TC026 is PASSED")
        else:
            log.error("User can not add texts in email TextBox - TC026 is FAILED")

    def test_tc027a(self):

        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)

        if App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("User can add texts in FirstName TextBox - TC019 is PASSED")
        else:
            log.error("User can not add texts in FirstName TextBox - TC019 is FAILED")

    def test_tc028a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow)

        if App_CustomerDetails.enter_in_lastname_txtbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("User can add texts in LastName TextBox - TC020 is PASSED")
        else:
            log.error("User can not add texts in LastName TextBox - TC020 is FAILED")

    def test_tc029a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_lastname_txtbox(self.driver, self.excel_obj, self.itestcaserow)

        if App_CustomerDetails.enter_in_address_txtbox(self.driver, self.excel_obj,self.itestcaserow):
            log.info("User can add texts in Address TextBox - TC021 is PASSED")
        else:
            log.error("User can not add texts in Address TextBox - TC021 is FAILED")

    def test_tc030a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_lastname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_address_txtbox(self.driver, self.excel_obj, self.itestcaserow)

        if App_CustomerDetails.enter_in_city_txtbox(self.driver, self.excel_obj,self.itestcaserow):
            log.info("User can add texts in City TextBox - TC022 is PASSED")
        else:
            log.error("User can not add texts in City TextBox - TC022 is FAILED")

    def test_tc031a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_lastname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_address_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_city_txtbox(self.driver, self.excel_obj, self.itestcaserow)

        if App_CustomerDetails.select_country(self.driver, self.excel_obj, self.itestcaserow):
            log.info("User can select a country - TC023 is PASSED")
        else:
            log.error("User can not select a country - TC023 is FAILED")

    def test_tc032a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_lastname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_address_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_city_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.select_country(self.driver, self.excel_obj, self.itestcaserow)

        if App_CustomerDetails.enter_in_phone_txtbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("User can add texts in Phone TextBox - TC024 is PASSED")
        else:
            log.error("User can not add texts in Phone TextBox - TC024 is FAILED")

    def test_tc033a(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_lastname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_address_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_city_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.select_country(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_phone_txtbox(self.driver, self.excel_obj, self.itestcaserow)

        if App_CustomerDetails.click_shipping_checkbox(self.driver):
            log.info("User can click on Same Shippin Address as Billing address checkbox - TC025 is PASSED")
        else:
            log.error("User can not click on Same Shippin Address as Billing address checkbox - TC025 is FAILED")

    def test_tc034a(self):

        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)

        App_CustomerDetails.enter_in_email_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_firstname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_lastname_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_address_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_city_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.select_country(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.enter_in_phone_txtbox(self.driver, self.excel_obj, self.itestcaserow)
        App_CustomerDetails.click_shipping_checkbox(self.driver)

        if App_CustomerDetails.click_purchase_button(self.driver):
            log.info("User can click on Purchase button - TC026 is PASSED")
        else:
            log.error("User can not click on Purchase button - TC026 is FAILED")

    @pytest.mark.mytest
    def test_tc035(self):

        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.check_for_alert(self.driver)
        App_ProductSelection.click_on_go_to_cart_button(self.driver)

        App_VerifyPurchase.verify_name_and_price(self.driver)
        App_VerifyPurchase.click_continue_button(self.driver)

        time.sleep(5)
        if App_CustomerDetails.click_go_back_button(self.driver):
            log.info("TC035 PASSED")
        else:
            log.error("TC035 FAILED")

    def teardown_method(self):
        log.endtestcase()
        # self.driver.quit()

    def teardown_class(self):
        # self.driver.quit()
        pass

