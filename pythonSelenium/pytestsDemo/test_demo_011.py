import pytest


# we can use fixture for drive the data
# Going to create new fixture inside 'conftest.py'
# 'dataLoad()'

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self,dataLoad):
        # we're returning something from fixture, then it is mandatory to pass fixture
        # as argument in test method
        print(dataLoad)
        print(f"First name : {dataLoad[0]}")
        print(f"Last name : {dataLoad[1]}")
        print(f"Email : {dataLoad[2]}")
