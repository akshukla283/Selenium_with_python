import pytest


# we can make it using scope level
# we want to execute fixture once before the class and after all the testcase got executed in the class
# then we need to simply go to 'conftest.py' file pass argument in fixture scope = "class"
# now pytest read scope and execute fixture based on that
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")


    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo method")


    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo method")