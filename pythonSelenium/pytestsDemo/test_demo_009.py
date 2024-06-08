import pytest


# using fixture at class level, as we have already defined 'setup' fixtures in 'conftest.py'
# using that with fixture
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