#!/usr/bin/env python3

"""
JSON Database Handler for WordTrixManager

This script provides functions to load and save a list of words in JSON format.
It includes utility functions for file-based data persistence and a test suite to validate these functions.

Functions:
- load: Loads words from a specified JSON file.
- save: Saves words to a specified JSON file.
- testsuite__database: A simple suite of test cases to verify the functionality of load and save functions.

Author: ChKimmling
Date: 13.11.2024
"""

import os
import json


def load(file: str) -> str:
    """
    Load words from a JSON file.
    
    Parameters:
    - file (str): Path to the JSON file from which to load words.
    
    Returns:
    - list: The list of words loaded from the JSON file, or an empty list if the file doesn't exist.
    """
    if os.path.exists(file):
        with open(file, "r") as file:
            return json.load(file)
    return []


def save(file: str, words: str) -> None:
    """
    Save words to a JSON file.
    
    Parameters:
    - file (str): Path to the JSON file in which to save words.
    - words (list): The list of words to save.
    
    Returns:
    - None
    """
    with open(file, "w") as file:
        json.dump(words, file, indent=4)


###############################################################################
# Test section

def testsuite__database():
    """
    Test suite to verify the load and save functions for JSON file handling.

    - Test case 1: Verifies that loading a non-existing file returns an empty list.
    - Test case 2: Checks that saving and loading a file returns the expected content.
    - Test case 3: Negative test to ensure that loading incorrect content does not pass.

    Returns:
    - None
    """
    # Testsuite setup
    _test_expected_text: str = "This is my convenient Test string."
    _test_unexpected_text: str = "This is my inconvenient Test string."
    _test_file1: str = "test1.file"
    _test_file2: str = "test2.file"

    # TESTCASE 01: Check for load of non-existing file
    assert [] == load(_test_file1), "Failed: Loading non-existing file should return an empty list."

    # TESTCASE 02: Check for save and load
    save(_test_file1, _test_expected_text)
    _loaded_text = load(_test_file1)
    assert _loaded_text == _test_expected_text, "Failed: Saved and loaded text does not match expected text."

    # TESTCASE 03: Check for save and load (NEGATIVE TEST)
    save(_test_file2, _test_expected_text)
    _loaded_text = load(_test_file2)
    assert _loaded_text != _test_unexpected_text, "Failed: Loaded text should not match unexpected text."

    # Testsuite cleanup
    os.remove(_test_file1)
    os.remove(_test_file2)

# Execute tests if the script is called directly
if __name__ == "__main__":
    testsuite__database()
