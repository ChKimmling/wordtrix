#!/usr/bin/env python3

"""
WordTrixManager: A Command-line Tool for Managing Anagram Pairs

This script provides an interactive mode and a non-interactive mode for managing a database of anagram pairs.
Users can check for anagrams, match existing entries, list stored entries, delete entries, and clear all entries.

Dependencies:
- wt_database (database management for storing/retrieving words)
- wt_methods_anagram (provides methods to check anagram relationships)

Usage:
- Interactive mode: Start the script without parameters to enter the interactive command line interface.
- Non-Interactive mode: Use the do_wordtrix function with specified operations.

Classes:
- WordTrixManager: Command line interface to manage anagram pairs.
Functions:
- do_wordtrix: A non-interactive function to perform operations directly from the script.

Author: ChKimmling
Date: 13.11.2024
"""

import cmd
from wt_database import wt_database as db
from wt_methods import wt_methods_anagram as anagram

###############################################################################
# Interactive mode

class WordTrixManager(cmd.Cmd):
    """
    Command-line manager for handling anagram operations and database storage.
    
    Attributes:
    - intro (str): Welcome message for the user.
    - prompt (str): Command prompt indicator.
    - file_name (str): Filename for JSON database of words.
    """

    intro = "Welcome to the Wordtrix. Type help or ? to list commands.\n"
    prompt = "(wordtrix) "
    file_name = "words.json"


    def __init__(self):
        """Initialize the WordTrixManager with word database loading."""
        super().__init__()
        self.words = db.load(WordTrixManager.file_name)


    def __del__(self):
        """Save the word database upon deletion of the instance."""
        db.save(WordTrixManager.file_name, self.words)


    def print_help_on_error(self):
        """Display a message when a command fails."""
        print("FAILED: Type help or ? to list commands.")


    def do_anagram_check(self, arg):
        """Check two text objects for anagram: anagram_check <subject1>, <subject2>"""
        if arg:
            try:
                subjects = arg.split(",")
                if anagram.is_anagram(subjects[0], subjects[1]):
                    self.words.append({"subject1": subjects[0], "subject2": subjects[1]})
                    print(f"Anagram found. Row added: {self.words}")
                else:
                    print(f"No anagram found on >>{subjects[0]}<< >>{subjects[1]}<<")
            except IndexError:
                self.print_help_on_error()
        else:
            self.print_help_on_error()


    def do_anagram_match(self, arg):
        """Check a subject for an anagram in the list: anagram_match <subject>"""
        if arg:
            _anagram_match = False
            for idx, word in enumerate(self.words, 1):
                subject1 = word['subject1']
                if anagram.is_anagram(arg, subject1):
                    _anagram_match = True
                    print(f"Match for >>{arg}<< found at {idx}. row: >>{subject1}<< >>{word['subject2']}<<")
            if not _anagram_match:
                print(f"No anagram found in db for >>{arg}<<")
        else:
            self.print_help_on_error()


    def do_list(self, arg):
        """List all stored words."""
        if not self.words:
            print("No words available.")
        else:
            for idx, words in enumerate(self.words, 1):
                print(f"{idx}. {words['subject1']} {words['subject2']}")


    def do_delete(self, arg):
        """Delete a word entry by specifying the row number: delete <row_number>"""
        try:
            index = int(arg) - 1
            if 0 <= index < len(self.words):
                word = self.words.pop(index)
                print(f"Deleted {index + 1}. row: {word['subject1']} {word['subject2']}")
            else:
                print("Invalid row number.")
        except ValueError:
            print("Please provide a valid row number.")


    def do_exit(self, arg):
        """Exit the Words Manager."""
        print("Exiting Words Manager.")
        return True


    def do_clear(self, arg):
        """Clear all words (cannot be undone) with confirmation."""
        confirmation = input("Are you sure you want to clear all words? (y/n): ")
        if confirmation.lower() == 'y':
            self.words = []
            print("All words cleared.")
        else:
            print("Clear aborted.")


###############################################################################
# Non-Interactive Mode

def do_wordtrix(operation: str, subject1: str = "", subject2: str = ""):
    """
    Perform non-interactive wordtrix operations based on the specified operation.

    Parameters:
    - operation (str): The operation to perform ('list', 'clear', 'check', or 'match').
    - subject1 (str): The first subject for anagram operations.
    - subject2 (str): The second subject for anagram check.
    """
        
    # Create WordTrixManager instance
    wordtrix = WordTrixManager()
    print(f"{wordtrix.intro.split('.')[0]}.\n")

    # Select operations
    if operation == "list":
        wordtrix.do_list(None)
    elif operation == "clear":
        wordtrix.do_clear()
    elif operation == "check":
        wordtrix.do_anagram_check(f"{subject1},{subject2}")
    elif operation == "match":
        wordtrix.do_anagram_match(f"{subject1}")
    else:
        print(f"FAILED: Unsupported operation >>{operation}<<.")
