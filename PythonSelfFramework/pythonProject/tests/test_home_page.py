import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.home_page_data import HomePageData
from pageObjects.home_page import HomePage
from utils.base_class import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        time.sleep(3)
        self.driver.refresh()

    # uncomment below and comment next method to run test from  class data
    ## test_HomePage_data = [{"firstname":"Ankit","lastname":"Shukla","gender":"Male"}, {"firstname":"Cameron", "lastname":"Diaz", "gender":"Female"}

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

    # @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    # def getData(self, request):
    #     return request.param

