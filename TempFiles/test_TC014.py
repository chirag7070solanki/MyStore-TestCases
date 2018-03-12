import pytest
from MyStore.Utilities import utils, Excel, log,constants
from MyStore.POM import Page_HomePage, Page_LogIn,Page_ProductListing, Page_CheckOut
from MyStore.appModules import SigIn, App_ProductSelection, App_VerifyPurchase

class Test_TC014:

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

    def test_verify_price(self):
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
            log.info("Product name and price verification successful - " + self.getclassname() + " is PASSED")
        else:
            log.error("Product name and price verification Unsuccessful - " + self.getclassname() + " is FAILED")

    def teardown_class(self):
        log.endtestcase()
        self.driver.quit()

