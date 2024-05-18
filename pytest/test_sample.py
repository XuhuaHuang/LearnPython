# Hands on with pytest framework
# Author: Xuhua Huang
#
# Last updated: July 8, 2021
# Created on: July 8, 2021


def increment_by_one(x: int):
    return x + 1


def test_increment():
    assert increment_by_one(3) == 5
