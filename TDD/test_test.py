from main import *
import pytest

@pytest.fixture()
def setup1():
    print("\nSetup1")
    yield
    print("\nTeardown")


@pytest.fixture()
def setup2():
    print("\nSetup2")
    def teardown_a():
        print("\nTeardown A")
    def teardown_b():
        print("\nTeardown B")
    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("Executing test 1")
    assert True


def test2(setup2):
    print("Executing test 2")
    assert True
