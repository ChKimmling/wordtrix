#!/usr/bin/env python3

"""
Anagram Checker Utility for WordTrixManager

This script provides a function to check if two strings are anagrams of each other.
It also includes a test suite to validate the anagram-checking functionality.

Functions:
- is_anagram: Determines if two strings are anagrams, with an optional case-sensitive check.
- testsuite__anagram: A series of test cases to validate the is_anagram function.

Author: ChKimmling
Date: 13.11.2024
"""

def is_anagram(subject1: str, subject2: str, case_sensitive: bool = False) -> bool:
    """
    Check if two strings are anagrams of each other.

    Parameters:
    - subject1 (str): The first string to compare.
    - subject2 (str): The second string to compare.
    - case_sensitive (bool): If True, the comparison is case-sensitive. Default is False.

    Returns:
    - bool: True if the strings are anagrams, False otherwise.
    """

    # Remove spaces for accurate comparison
    subject1 = subject1.replace(" ", "")
    subject2 = subject2.replace(" ", "")
    
    # Convert to lowercase if case sensitivity is disabled
    if not case_sensitive:
        subject1 = subject1.lower()
        subject2 = subject2.lower()

    # Sort the characters of each string and compare
    _subject1_list = sorted(subject1)
    _subject2_list = sorted(subject2)

    return _subject1_list == _subject2_list

###############################################################################
# Test section

def testsuite__anagram() -> None:
    """
    Test suite to validate the is_anagram function.

    - Test case 1: Checks if two matching anagram strings return True.
    - Test case 2: Checks that non-anagram strings return False.
    - Test case 3: Verifies that case-sensitive comparison works correctly.

    Returns:
    - None
    """

    # TESTCASE 01: Check for matching anagram strings (case-insensitive)
    assert is_anagram("listen listen", "silent Silent"), "Failed: Expected anagram match."

    # TESTCASE 02: Check for non-matching anagram strings
    assert not is_anagram("listen", "hear"), "Failed: Expected no anagram match."

    # TESTCASE 03: Check for non-matching anagram strings (case-sensitive)
    assert not is_anagram("listen", "Silent", True), "Failed: Expected no match with case-sensitive check."

# Execute tests if the script is called directly
if __name__ == "__main__":
    testsuite__anagram()
