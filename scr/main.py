from __future__ import print_function
import argparse

"""
SCR Frontend command line executable.
"""

def main(argv=None):
    """This is the entry point for the SCR command.

    Args:
        argv (list of str or None): command line arguments, NOT including
           the executable name. If None, parses from sys.argv.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-h', '--help',
        dest='help', action=''
        help="show this help message and exit"
    )
