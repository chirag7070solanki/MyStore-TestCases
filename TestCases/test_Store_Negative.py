import pytest, unittest
from MyStore.Utilities import utils, Excel, log
from MyStore.appModules import SigIn, App_ProductSelection, App_VerifyPurchase, App_CustomerDetails
import time


class Test_TC001:

    def setup_class(self):
        self.excel_obj = Excel.Excel()
        self.excel_obj.setexcelfile()
        self.itestcaserow = Excel.Excel.get_row_num(self.excel_obj, "Test3")

    def setup_method(self):
        log.starttestcase()
        self.driver = utils.openbrowser(self.excel_obj, self.itestcaserow)

    def test_tc007(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        if SigIn.wrong_login(self.driver):
            log.info("TC007 is PASSED")
        else:
            log.error("TC007 is FAILED")

    def test_tc008(self):
        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        if SigIn.click_lost_password(self.driver):
            log.info("TC008 is PASSED")
        else:
            log.error("TC008 is FAILED")

    def teardown_method(self):
        log.endtestcase()
        # self.driver.quit()

    def teardown_class(self):
        # self.driver.quit()
        pass