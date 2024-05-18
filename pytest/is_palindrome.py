# -*- coding: utf-8 -*-

from re import sub

def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome.

    Args:
        word (str): Word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    # Normalize the string: convert to lowercase
    word = word.lower()

    # Remove non-alphanumeric characters using regular expressions
    # An alternative approach would be using the isalnum() method from Python
    word = sub(r'[^a-z0-9]', '', word)

    # Check if the string is equal to its reverse
    return word == word[::-1]
