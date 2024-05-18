"""
Test is_palindrome function with parameters that are palindromes.
"""

from is_palindrome import is_palindrome

import pytest


@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",
])
def test_is_palindrome(palindrome: str):
    """Test is_palindrome function with parameters that are palindromes.

    Args:
        palindrome (str): Palindrome strings to test.
    """
    assert is_palindrome(palindrome)


@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome: str):
    """Test is_palindrome function with parameters that are not palindromes.

    Args:
        non_palindrome (str): Non-palindrome strings to test.
    """
    assert not is_palindrome(non_palindrome)


if __name__ == "__main__":
    pytest.main()
