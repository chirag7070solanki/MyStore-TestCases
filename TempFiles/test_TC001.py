import pytest
from MyStore.Utilities import utils, Excel, log
from MyStore.POM import Page_HomePage
from MyStore.appModules import SigIn, App_ProductSelection, App_VerifyPurchase, App_CustomerDetails
import time


class Test_TC001:

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

    def test_sign_in(self):
        if SigIn.click_my_account_button(self.driver):
            log.info("My Account element is clickable - " + self.getclassname() + " is PASSED")
        else:
            log.error("Element is not clickable" + self.getclassname() + " is FAILED")

    def teardown_class(self):
        log.endtestcase()
        self.driver.quit()

