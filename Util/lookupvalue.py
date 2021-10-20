# Topic: Look up by value in a dictionary
#
# Author: Xuhua Huang
# Last updated: Oct 20, 2021
# Created on: Oct 20, 2021

from typing import Any


def lookup_by_value(_dict: dict, value: Any):
    return list(_dict.keys())[list(_dict.values()).index(value)]
