#!/usr/bin/env python3

"""
WordTrixManager: A Command-line Tool for Managing Anagram Pairs

This script provides an interactive mode and a non-interactive mode for 
managing a database of anagram pairs. Users can check for anagrams, 
match existing entries, list stored entries, delete entries, and clear all entries.

Author: ChKimmling
Date: 13.11.2024
"""

import cmd
from wordtrix.wt_database import wt_database as db
from wordtrix.wt_methods import wt_methods_anagram as anagram

###############################################################################
# Interactive mode

class WordTrixManager(cmd.Cmd):
    """
    Command-line manager for handling anagram operations and database storage.
    """

    intro = "Welcome to the Wordtrix. Type help or ? to list commands.\n"
    prompt = "(wordtrix) "
    file_name = "words.json"


    def __init__(self):
        """Initialize the WordTrixManager with word database loading."""

        super().__init__()
        self.words = db.load(WordTrixManager.file_name)


    def __del__(self) -> None:
        """Save the word database upon deletion of the instance."""

        db.save(WordTrixManager.file_name, self.words)


    def print_help_on_error(self) -> None:
        """Display a message when a command fails."""

        print("FAILED: Type help or ? to list commands.")


    def do_anagram_check(self, arg: str) -> None:
        """Check two text objects for anagram: anagram_check <subject1>, <subject2>"""

        if arg:
            try:
                _subjects = arg.split(",")
                if anagram.is_anagram(_subjects[0], _subjects[1]):
                    self.words.append({"subject1": _subjects[0], "subject2": _subjects[1]})
                    print(f"Anagram found. Row added: {self.words}")
                else:
                    print(f"No anagram found on >>{_subjects[0]}<< >>{_subjects[1]}<<")
            except IndexError:
                self.print_help_on_error()
        else:
            self.print_help_on_error()


    def do_anagram_match(self, arg: str) -> None:
        """Check a subject for an anagram in the list: anagram_match <subject>"""

        if arg:
            _anagram_match = False
            for _idx, _word in enumerate(self.words, 1):
                _subject1 = _word['subject1']
                if anagram.is_anagram(arg, _subject1):
                    _anagram_match = True
                    print(f"Match for >>{arg}<< found at {_idx}. row: ")
                    print(f"  >>{_subject1}<< >>{_word['subject2']}<<")
            if not _anagram_match:
                print(f"No anagram found in db for >>{arg}<<")
        else:
            self.print_help_on_error()


    def do_list(self, _arg: str) -> None:
        """List all stored words."""

        if not self.words:
            print("No words available.")
        else:
            for _idx, _words in enumerate(self.words, 1):
                print(f"{_idx}. {_words['subject1']} {_words['subject2']}")


    def do_delete(self, arg: str) -> None:
        """Delete a word entry by specifying the row number: delete <row_number>"""

        try:
            _index = int(arg) - 1
            if 0 <= _index < len(self.words):
                _word = self.words.pop(_index)
                print(f"Deleted {_index + 1}. row: {_word['subject1']} {_word['subject2']}")
            else:
                print("Invalid row number.")
        except ValueError:
            print("Please provide a valid row number.")


    def do_exit(self, _arg: str) -> None:
        """Exit the Words Manager."""

        print("Exiting Words Manager.")
        return True


    def do_clear(self, _arg: str) -> None:
        """Clear all words (cannot be undone) with confirmation."""

        _confirmation = input("Are you sure you want to clear all words? (y/n): ")
        if _confirmation.lower() == 'y':
            self.words = []
            print("All words cleared.")
        else:
            print("Clear aborted.")


###############################################################################
# Non-Interactive Mode

def do_wordtrix(operation: str, subject1: str = "", subject2: str = "") -> None:
    """
    Perform non-interactive wordtrix operations based on the specified operation.

    Parameters:
    - operation (str): The operation to perform ('list', 'clear', 'check', or 'match').
    - subject1 (str): The first subject for anagram operations.
    - subject2 (str): The second subject for anagram check.
    """

    # Create WordTrixManager instance
    _wordtrix = WordTrixManager()
    print(f"{_wordtrix.intro.split('.')[0]}.\n")

    # Select operations
    if operation == "list":
        _wordtrix.do_list(None)
    elif operation == "clear":
        _wordtrix.do_clear(None)
    elif operation == "check":
        _wordtrix.do_anagram_check(f"{subject1},{subject2}")
    elif operation == "match":
        _wordtrix.do_anagram_match(f"{subject1}")
    else:
        print(f"FAILED: Unsupported operation >>{operation}<<.")
