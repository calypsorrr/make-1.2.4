#!/usr/bin/env python
"""
Info about our project comes here
"""

import os

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

# will do the command (ifconfig) in the terminal
def main_ip():
    os.system("ifconfig")



if __name__ == '__main__':  # code to execute if called from command-line
    main_ip()
