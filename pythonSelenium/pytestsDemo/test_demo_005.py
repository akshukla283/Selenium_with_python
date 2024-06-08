# to skip the testcase


import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed becacuse strings do not match"


def test_thirdCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"

