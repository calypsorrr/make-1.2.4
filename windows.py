#!/usr/bin/env python
"""
Info about our project comes here
"""

import platform

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

# Will print out the system, node, release, version, machine, processor
def main_windows():
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")
    print("\n")

if __name__ == '__main__':  # code to execute if called from command-line
    main_windows()
