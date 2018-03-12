import pytest, time
from MyStore.Utilities import utils, Excel, log,constants
from MyStore.POM import Page_HomePage, Page_LogIn,Page_ProductListing, Page_CheckOut, Page_CustomerDetails
from MyStore.appModules import SigIn, App_CustomerDetails,App_VerifyPurchase, App_ProductSelection


class Test_TC020:

    def getclassname(self):
        cls_name = __class__.__name__
        testcase = cls_name[5:]
        return testcase

    def setup_class(self):
        log.starttestcase()
        self.excel_obj = Excel.Excel()
        self.excel_obj.setexcelfile()
        self.itestcaserow = Excel.Excel.get_row_num(self.excel_obj, "Test2")
        self.driver = utils.openbrowser(self.excel_obj, self.itestcaserow)

    def test_city_textbox(self):
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
            log.info("User can add texts in City TextBox - " + self.getclassname() + " is PASSED")
        else:
            log.error("User can not add texts in City TextBox - " + self.getclassname() + " is FAILED")

    def teardown_class(self):
        log.endtestcase()
        self.driver.quit()

