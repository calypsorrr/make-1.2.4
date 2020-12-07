#!/usr/bin/env python
"""
Info about our project comes here
"""

import subprocess

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main_bash():
    print("start")
    subprocess.call("linux.sh")
    print("end")


if __name__ == '__main__':  # code to execute if called from command-line
    main_bash()
