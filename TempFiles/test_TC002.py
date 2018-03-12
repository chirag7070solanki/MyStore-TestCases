import pytest
from MyStore.Utilities import utils, Excel, log,constants
from MyStore.POM import Page_HomePage, Page_LogIn
from MyStore.appModules import SigIn, App_ProductSelection, App_VerifyPurchase, App_CustomerDetails
import time


class Test_TC002:

    bool_val = False

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

    def test_user_id(self):
        SigIn.click_my_account_button(self.driver)
        if SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("User ID TextBox is taking texts - " + self.getclassname() + " is PASSED")
        else:
            log.error("User ID TextBox is not taking texts - " + self.getclassname() + " is FAILED")

    def test_password_id(self):
        if SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow):
            log.info("Password TextBox is taking texts - " + self.getclassname() + " is PASSED")
        else:
            log.error("Password TextBox is not taking texts - " + self.getclassname() + " is FAILED")

    def teardown_class(self):
        log.endtestcase()
        self.driver.quit()

