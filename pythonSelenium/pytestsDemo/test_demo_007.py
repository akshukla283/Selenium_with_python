import pytest


# fixture in pytest
# In pytest, fixtures are a way to set up a fixed baseline state for tests. They can be used to provide the necessary context or state needed for the tests to run. Fixtures are especially useful for setting up things like database connections, test data, configuration settings, and more.
# Fixture Scope
# Fixtures can have different scopes which determine how often the fixture setup and teardown code is run. The available scopes are:
#
# function (default): The fixture is created and destroyed for each test function.
# class: The fixture is created and destroyed once per test class.
# module: The fixture is created and destroyed once per module.
# package: The fixture is created and destroyed once per package.
# session: The fixture is created and destroyed once per session.
# To specify the scope, use the scope parameter in the @pytest.fixture decorator:
# in the setup fixture we can 'yield' to teardown
# let's define fixture

@pytest.fixture()
def setup():
    print("\nI will be executing first from fixture")
    yield
    print("\nThis is post test method teardwon")


def test_fixtureDemo(setup):  # we inherited fixture
    print("I will execute steps in fixtureDemo method")