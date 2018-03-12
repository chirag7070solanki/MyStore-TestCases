from selenium import webdriver
from MyStore.Utilities import Excel, log, constants


def openbrowser(excel, itestcaserow):
    browser = Excel.Excel.get_content(excel, itestcaserow, constants.col_browser)
    wd = webdriver.Chrome("O:\JobTraining\QA\WebDrivers\\chromedriver.exe")
    wd.get("http://store.demoqa.com/")
    wd.maximize_window()
    wd.implicitly_wait(10)
    log.info("Browser opened")
    return wd

