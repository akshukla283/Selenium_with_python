# to run only testcase which identified as smoke
# need to mark that test with tag "@pytest.mark.smoke"
# to run that "pytest -m smoke -v -s"
# you will get some warning, ignore that for now, will about that later


import pytest
@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed becacuse strings do not match"


def test_thirdCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"

