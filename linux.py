#!/usr/bin/env python
"""
Info about our project comes here
"""

import platform

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

# Will print out architecture, machine, node, system, processors
def main_linux():
    # Architecture
    print("Architecture: " + platform.architecture()[0])

    # machine
    print("Machine: " + platform.machine())

    # node
    print("Node: " + platform.node())

    # system
    print("System: " + platform.system())

    # processors
    print("Processors: ")
    with open("/proc/cpuinfo", "r")  as f:
        info = f.readlines()

    cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
    for index, item in enumerate(cpuinfo):
        print("    " + str(index) + ": " + item)

if __name__ == '__main__':  # code to execute if called from command-line
    main_linux()
