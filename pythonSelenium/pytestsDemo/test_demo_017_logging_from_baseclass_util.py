import pytest
from pytestsDemo.base_class import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample3(BaseClass):
    def test_loggin_from_util_Baseclass(self,dataLoad):
        tlogger = self.getLogger()
        # now we need to use 'tlogger' instead of print to log the message
        tlogger.info(dataLoad)
        tlogger.info(f"First name : {dataLoad[0]}")
        tlogger.info(f"Last name : {dataLoad[1]}")
        tlogger.info(f"Email : {dataLoad[2]}")
        # printing some message from this class also
        tlogger.info("This is from test class 'TestExample3' and test method 'test_loggin_from_util_Baseclass'")

# below we can see it is showing name message from baseclass
# that we will handle in next test from BaseClass itself
"""
2024-06-05 18:35:58,332 :INFO :pytestsDemo.base_class : First name : Ankit
2024-06-05 18:35:58,332 :INFO :pytestsDemo.base_class : Last name : Shukla
2024-06-05 18:35:58,332 :INFO :pytestsDemo.base_class : Email : akshukla@gmail.com
"""