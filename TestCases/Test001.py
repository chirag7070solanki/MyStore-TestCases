import pytest
from MyStore.Utilities import utils, Excel, log
from MyStore.appModules import SigIn, App_ProductSelection, App_VerifyPurchase, App_CustomerDetails
import time


class Test001:
    def setup_class(self):
        # This is a SetUp class method
        # Webdriver instance is created, URL loaded
        # Excel sheet for TestData is initialized/opened

        self.excel_obj = Excel.Excel()
        self.excel_obj.setexcelfile()
        self.itestcaserow = Excel.Excel.get_row_num(self.excel_obj, "Test2")
        log.starttestcase()
        self.driver = utils.openbrowser(self.excel_obj, self.itestcaserow)

    # @pytest.mark.test
    def test_signin(self):
        # This module is to Test LogIn functionality of an Application
        # What has to be done for successful login is given in AppModule-SigIn

        SigIn.attempsignin(self.excel_obj, self.driver, self.itestcaserow)

    def test_Productselection(self):
        # This module is to Test ProductSelection
        # Which product to select comes from Test Datasheet
        # What numbered product to select from available products also comes from DataSheet.

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_product_no(self.excel_obj, self.driver, self.itestcaserow)

    # @pytest.mark.test
    def test_purchaseverify(self):

        # This module is for Product verification - We need to verify Name and Price of a product before
        # moving forward

        App_VerifyPurchase.check_product_details(self.driver)

    # @pytest.mark.test
    def test_customerdetails(self):
        # This module is to enter customer details
        time.sleep(5)
        App_CustomerDetails.customer_details(self.excel_obj, self.driver, self.itestcaserow)

    def teardown_class(self):
        self.driver.quit()

