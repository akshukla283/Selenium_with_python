import pytest


# @pytest.fixture()
@pytest.fixture(scope="class")
def setup():
    print("\nI will be executing first from fixture")
    yield
    print("\nThis is post test method teardwon")


# writing fiture to return data
@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Ankit", "Shukla", "akshukla@gmail.com"]


# parameterized test fixture
# to send data we need to use parameter "request"
# which is instance of the fixture
# @pytest.fixture(params=["Chrome", "Firefox", "Edge"])
@pytest.fixture(
    params=[("Chrome", "Ankit"), ("Firefox", "Shukla"), ("Edge", "akshukla@gmail.com")])  # we wrap some data in tuple that will be part of first execution
def crossBroser(request):  # 'request' is an instance of fixture to send data
    return request.param
