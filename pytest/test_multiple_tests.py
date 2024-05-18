# Hands on with pytest framework
# Running multiple tests with CLI
# Author: Xuhua Huang
#
# Last updated: July 10, 2021
# Created on: July 10, 2021

import pytest

"""
pytest will run all all files of the form of the following:
"test_*.py" or "*_test.py" in the current directory
following generally test discovery rules
"""


def force_crash():
    raise SystemExit(1)


def test_force_crash():
    with pytest.raises(SystemExit):
        force_crash()


# Group multiple tests in a class
# pytest will discover both methods prefixed with "test_*"
class TestClass:
    def test_one(self):
        some_str = "This is a simple string"
        assert 'h' in some_str

    def test_two(self):
        classic = 'Hello, world'
        try:
            assert hasattr(classic, 'check')
        except AssertionError:
            print('An expected assertion error has occurred in method test_two')


@pytest.mark.custom
def test_mark():
    print('This is a customized pytest mark to run')
    assert True
