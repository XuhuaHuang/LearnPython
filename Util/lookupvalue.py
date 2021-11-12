# Topic: Look up by value in a dictionary
#
# Author: Xuhua Huang
# Last updated: Oct 20, 2021
# Created on: Oct 20, 2021

from typing import Any, Optional


def lookup_by_value(_dict: dict, value: Any) -> Optional[Any]:
    # Using the .keys() method to collect all dictionary keys and convert to a list
    # then use the [] operator on the constructed list
    # with the .index() method on all colected dictionary values to find key value
    return list(_dict.keys())[list(_dict.values()).index(value)]
