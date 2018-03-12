import pytest, unittest
from MyStore.Utilities import utils, Excel, log
from MyStore.appModules import SigIn, App_ProductSelection, App_VerifyPurchase, App_CustomerDetails
import time


class Test_TC001:

    def setup_class(self):
        self.excel_obj = Excel.Excel()
        self.excel_obj.setexcelfile()
        self.itestcaserow = Excel.Excel.get_row_num(self.excel_obj, "Test5")

    def setup_method(self):
        log.starttestcase()
        self.driver = utils.openbrowser(self.excel_obj, self.itestcaserow)

    def test_tc018(self):

        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_single_product_name(self.driver, self.excel_obj, self.itestcaserow)

        if App_ProductSelection.click_product_name_Add_to_cart(self.driver):
            log.info("TC018 PASSED")
        else:
            log.error("TC018 FAILED")

    def test_tc019(self):

        SigIn.click_my_account_button(self.driver)
        SigIn.enter_text_in_user_id_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.enter_text_in_password_textbox(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.click_login_button(self.driver)
        SigIn.check_for_successful_login(self.driver, self.excel_obj, self.itestcaserow)
        SigIn.check_for_logout_button(self.driver)

        App_ProductSelection.select_a_product(self.excel_obj, self.driver, self.itestcaserow)
        App_ProductSelection.select_a_single_product_name(self.driver, self.excel_obj, self.itestcaserow)

        if App_ProductSelection.click_like(self.driver):
            log.info("TC019 PASSED")
        else:
            log.error("TC019 FAILED")

    def teardown_method(self):
        log.endtestcase()
        self.driver.quit()

    def teardown_class(self):
        # self.driver.quit()
        pass
