import pytest
from MyStore.Utilities import utils, Excel, log,constants
from MyStore.POM import Page_HomePage, Page_LogIn
from MyStore.appModules import SigIn


class Test_TC004:

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

    def test_SignIn_username(self):

        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)

        if SigIn.check_for_successful_login(self.driver, self.excel_obj,self.itestcaserow):
            log.info("LogIn Successful - " + self.getclassname() + " is PASSED")
        else:
            log.info("LogIn Unsuccessful - " + self.getclassname() + " is FAILED")

    def teardown_class(self):
        log.endtestcase()
        self.driver.quit()

