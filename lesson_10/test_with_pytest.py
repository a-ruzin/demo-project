import pytest


def func(x):
    return x + 1


# -------------------------
def test_func():
    assert func(3) == 4
    # assert func(4) == 6

def test_func2(tmpdir):
    print('ho-ho-ho', tmpdir)
    assert func(3) == 4


# -------------------------
class TestClass:
    def test_func(self):
        assert func(3) == 4
        # assert func(4) == 6

    def test_func2(self, tmpdir):
        print('ho-ho-ho', tmpdir)
        assert func(3) == 4


# -------------------------
@pytest.fixture
def randomfixture():
    import random
    return random.randint(1,10), random.randint(1,10), random.randint(1,10)


def test_fixture(randomfixture):
    print(randomfixture)


def test_fixture2(randomfixture):
    print(randomfixture)

# scope="module"

@pytest.fixture(scope="module")
def randomfixture2(request):
    import random
    print('setup randomfixture2 {}'.format(request))
    yield random.randint(1,10), random.randint(1,10), random.randint(1,10)
    print('teardown randomfixture2')

def test_fixture3(randomfixture2):
    print(randomfixture2)


def test_fixture4(randomfixture2):
    print(randomfixture2)


# --------------------
class ProductionClass():
    def method(self, *args):
        return args

from unittest.mock import MagicMock

def test_mock():
    thing = ProductionClass()
    print(thing.method(1, 2, 3, 4))
    thing.method = MagicMock(return_value=3)
    print(thing.method(3, 4, 5, 'value'))
    assert thing.method(3, 4, 5, 'value') == 3
