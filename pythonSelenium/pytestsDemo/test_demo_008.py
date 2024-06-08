import pytest


# fixture in pytest
# suppose there are multiple test for which
# we need some common steps, so reduce the code and all
# we can write a common fixture in file pytest file 'coftest.py'
# in that file we need to define that common fixture
# when we run test it will check setup first as we inherited it
# and it won't find the fixture here then it will look for 'conftest.py' file and take fixture from there

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")