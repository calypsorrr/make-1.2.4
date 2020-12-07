#!/usr/bin/env python
"""
Info about our project comes here
"""

import subprocess

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main_upgrade():
    print("start")
    subprocess.call("install3.sh")
    print("end")


if __name__ == '__main__':  # code to execute if called from command-line
    main_upgrade()
