# Topic: Determine whether a string is a palindrome
# Spells the same even the string is reversed
# File: palindrome.py
#
# Author: Xuhua Huang
# Last updated: Oct 21, 2021
# Created on: Oct 21, 2021

# Return True if input is a palindrome using only alphanumeric characters
# ignoring case and spaces
def is_palindrome(s: str) -> bool:
    s_comp: str = ''.join(char for char in s if char.isalnum()).lower()
    # using generators to iterate through the string
    # identify alphanumeric characters and convert them to lower case
    # append them to a newly constructed string and assign to s_comp
    return s_comp[::-1] == s_comp


def main():
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))  # False
    print(is_palindrome("My 2 tests are pass! :) ssap era stset 2 ym"))  # True


if __name__ == "__main__":
    main()
