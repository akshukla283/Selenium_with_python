# to skip the testcase
# there is other requirement, suppose you skipped the test but there
# are some prerequisites inside that test which is needed in next test
# we know this test getting fail but we have to execute till prerequisites
# we can skip this failre in report
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.xfail  # it will fail but not report in result
def test_thirdCreditCard():
    a = 10
    b = 6
    assert a + 2 == b, "Addition do not match"

# pytest test_demo_006.py -vs
# you saw that it executed but not reported
