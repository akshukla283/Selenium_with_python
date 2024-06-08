import pytest


# to run particular method/test from multiple file
# suppose we have to run all test case having 'CreditCard' in method name
# we need to pass '-k' keyword name to detect the selected module name
# pytest -k CreditCard -v -s
# method name should have sense
# '-k' for method name
# '-s' for loging , '-v' for more info metadata

def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed becacuse strings do not match"


@pytest.mark.smoke  # marking as smoke for next lecture
def test_thirdCreditCard():
    a = 4
    b = 6
    assert a + 2 == b, "Addition do not match"
