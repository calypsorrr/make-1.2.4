#!/usr/bin/env python
"""
Info about our project comes here
"""

from subprocess import call

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

# Reads update.save (bash) and do the functions in the terminal one for one
def main_bash():
    with open("update.save", "rb") as file:
        script = file.read()
    rc = call(script, shell=True)


if __name__ == '__main__':  # code to execute if called from command-line
    main_bash()
