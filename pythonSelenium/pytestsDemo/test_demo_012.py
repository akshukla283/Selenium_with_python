import pytest


# we can use fixture for drive the data

# suppose we want to test selenium automation in different browser

# crassBrowser will execute as number of time as much element pass in 'params'
# datadriven and parameterization can be done with return statement in list of tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

def test_crassBrowser(crossBroser): # we haven't pass self because it not in class now
    print(crossBroser[1]) # we can use index



"""
test_demo_012.py::test_crassBrowser[crossBroser0] ('Chrome', 'Ankit')
PASSED
test_demo_012.py::test_crassBrowser[Firefox] Firefox
PASSED
test_demo_012.py::test_crassBrowser[Edge] Edge
PASSED
"""