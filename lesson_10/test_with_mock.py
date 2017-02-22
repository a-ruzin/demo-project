from unittest.mock import MagicMock, Mock, patch, sentinel

# -------------------- правка конкретного метода
import pytest


class MyClass():
    def my_method(self, *args):
        return args


def test_mock():
    thing = MyClass()
    print(thing.my_method(1, 2, 3, 4))

    thing.my_method = MagicMock(return_value=3)
    print(thing.my_method(3, 4, 5, 'value'))

    assert thing.my_method(3, 4, 5, 'value') == 3

    # args = [3, 4, 5, 'value']
    # assert thing.my_method(*args) == args


# -------------------- assert_called_once_with для SUT
class MyClass2():
    def outter_method(self, a, b, c):
        return self.inner_method(a, b), c

    def inner_method(self, a, b):
        return a+b


def test_mock2():
    thing = MyClass2()
    thing.inner_method = MagicMock()
    thing.outter_method(1, 2, 3)
    thing.inner_method.assert_called_once_with(1, 2)



# -------------------- assert_called_with для объекта переданного в SUT
class MyClass3():
    def do_something(self, obj):
        return obj.call_method()


def test_mock3():
    thing = MyClass3()
    mock = Mock()
    thing.do_something(mock)
    mock.call_method.assert_called_with()


# ----------------- return_value
import collections


def some_function():
    instance = collections.defaultdict(list)
    instance[4] = 17  # == instance.__setitem__(4, 17)
    return instance[3]  # == instance.__getitem__(3)


def test_mock4():
    # print('before patch defaultdict:', type(collections.defaultdict()))
    with patch('collections.defaultdict') as mocked_dict:
        # print('in patch defaultdict:', type(collections.defaultdict()))
        mocked_dict.return_value.__getitem__.return_value = []
        assert some_function() == []
        mocked_dict.return_value.__setitem__.assert_called_with(4, 17)
    # print('after patch defaultdict:', type(collections.defaultdict()))


# ------------- side_effect
def test_mock5():
    mock = MagicMock(side_effect=ValueError('ho-ho'))
    with pytest.raises(ValueError) as excinfo:
        mock()
    assert 'ho-ho' in str(excinfo.value)


# ------------- side_effect
def test_mock6():
    mock = MagicMock(side_effect=range(10))
    with pytest.raises(StopIteration):
        while True:
            mock()


# ------------- side_effect
def test_mock7():
    mock = MagicMock(side_effect=[1, 2, 3])
    assert mock() == 1
    assert mock() == 2
    assert mock() == 3


# ------------- side_effect
def test_mock8():

    def my_callable(*args):
        vals = {(1, 3): 2, (3,): 4}
        return vals[args]

    mock = MagicMock(side_effect=my_callable)
    mock(3)
    mock(1, 3)
    mock(3)
    mock(1, 3)
    # mock(1)


# ------------- spec
def test_mock9():
    mock = MagicMock()
    mock.call_me_once()

    mock = MagicMock(spec=collections.defaultdict)
    mock.__getitem__ = lambda x, y: '234'
    assert mock[3] == '234'
    # mock.call_me_once()


# --------------- @patch декоратор
@patch('lesson_05.answers.Employee.get_salary', lambda self: sentinel.salary)
def test():
    from lesson_05.answers import Employee
    e = Employee('Olga', 333)
    assert e.get_salary() == sentinel.salary
