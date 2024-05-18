# Hands on with pytest framework
# with assertion statement
# Author: Xuhua Huang
#
# Last updated: July 14, 2021
# Created on: July 14, 2021


import pytest
import unittest


def simple_fn():
    return 3


def test_simple_fn():
    assert simple_fn() == 4  # this will throw an AssertionError


# Specifying a message with the assertion
# this test is run with the following command:
# python -m pytest test_03_assertion.py::test_assert_msg
def test_assert_msg():
    assert simple_fn() == 3, "The assertion is true, the function returns value 3"


# Assertion with expected exceptions
def test_zerp_divisiob_err():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# ExceptionInfo.type, .value, and .traceback
def test_recursion_depth():
    # using pytest.raises() as context manager
    with pytest.raises(RuntimeError) as excinfo:
        # nobody should ever write this
        # for demonstration purpose only
        def recur():
            recur()

        recur()
    assert "maximum recursion" in str(excinfo.value)


# Assertion with expected warnings
# this test is run with the following command:
# python -m pytest test_03_assertion.py::test_set_comparison
def test_set_comparison():
    assert set("1308") == set("1655")


# using assertEqual function
# this test is run with the following command:
# python -m unittest test_03_assertion.MyUnitTest
class MyUnitTest(unittest.TestCase):
    def test_assertEqual_fn(self):
        self.assertEqual(True, True)
