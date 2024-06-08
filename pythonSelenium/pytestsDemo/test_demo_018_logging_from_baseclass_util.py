import pytest
from pytestsDemo.base_class import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample3(BaseClass):
    def test_loggin_from_util_Baseclass(self,dataLoad):
        tlogger = self.getLogger()
        tlogger.info(dataLoad)
        tlogger.info(f"First name : {dataLoad[0]}")
        tlogger.info(f"Last name : {dataLoad[1]}")
        tlogger.info(f"Email : {dataLoad[2]}")
        # printing some message from this class also
        tlogger.info("This is from test class 'TestExample3' and test method 'test_loggin_from_util_Baseclass'")

# in report.html all logger message will be logged
# let's creat report as well
# pytest test_demo_018_logging_from_baseclass_util.py -vs --html=demo_018_report.html