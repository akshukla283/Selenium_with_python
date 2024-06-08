# use flag '-s' and for detailed info '-v'
# to run only particular file then git just file with pytest
#  py.test test_demo002.py -v -s
# pytest test_demo002.py -v -s

def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed becacuse strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"

