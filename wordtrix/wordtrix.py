#!/usr/bin/env python3

"""
Command-Line Interface (CLI) for WordTrix Anagram Manager

This script serves as the CLI for interacting with the WordTrix anagram database.
It provides options for interactive mode, listing entries, clearing entries, 
checking if two words are anagrams, and finding matching anagrams from the database.
The argparse module is used to parse command-line arguments.

Author: ChKimmling
Date: 13.11.2024
"""

import argparse
from wordtrix.wt_manager import wt_manager_cli as cli


def parse_cli_arguments() -> argparse.Namespace:
    """
    Define and parse command-line arguments for WordTrixManager.
    """

    # Construct parser and define arguments
    parser = argparse.ArgumentParser(description="WordTrix Anagram Manager CLI")

    parser.add_argument("--interactive", help="Interactive mode.",
                        action="store_true", default=False)
    parser.add_argument("--list", help="List anagrams in db",
                        action="store_true")
    parser.add_argument("--clear", help="Clear anagrams in db",
                        action="store_true")
    parser.add_argument("--check", nargs=2, help="Check for anagram",
                        metavar=('sub1', 'sub2'))
    parser.add_argument("--match", nargs=1, help="Check for anagram match in db",
                        metavar='sub1')

    # Return parsed CLI arguments
    return parser.parse_args()


def main():
    """
    Main function to execute operations based on parsed command-line arguments.
    """

    cli_args = parse_cli_arguments()

    # Determine operation mode based on arguments
    if cli_args.interactive:
        try:
            cli.WordTrixManager().cmdloop()
        except KeyboardInterrupt:
            pass  # Gracefully handle interrupt in interactive mode
    elif cli_args.list:
        cli.do_wordtrix("list")
    elif cli_args.clear:
        cli.do_wordtrix("clear")
    elif cli_args.check:
        cli.do_wordtrix("check", cli_args.check[0], cli_args.check[1])
    elif cli_args.match:
        cli.do_wordtrix("match", cli_args.match[0])
    else:
        print("ERROR: Please select an operation mode. Use --help for usage.")


# Execute main function if the script is called directly
if __name__ == "__main__":
    main()
