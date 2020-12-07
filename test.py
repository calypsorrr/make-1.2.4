#!/usr/bin/env python
"""
Info about our project comes here
"""

from Calculator_flow import main_both
from password import main_password
from ip_adress import main_ip
from windows import main_windows
from linux import main_linux
from bash import main_bash
from bash_upgrade import main_upgrade

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

def main():
    while True:
        print("What function do you want to do")
        print("\n")
        print("1. IP weergave (LAN en/of WAN, eth0 en of wlan0)")
        print("2. Password generator")
        print("3. system update en upgrade (linux)")
        print("4. Software installatie (linux) vb.: Apache, MariaDB, PHP,")
        print("5. system info weergave windows")
        print("6. system info RPI")
        print("7. netwerk en/of poortscanner")
        print("8. gpio pin weergave en hun status")
        print("9. Calculator")

        user_1 = input()

        if user_1 == "1":
            main_ip()
            print("\n")
        elif user_1 == "2":
            main_password()
            print("\n")
        elif user_1 == "3":
            main_bash()
            print("\n")
        elif user_1 == "3":
            main_upgrade()
            print("\n")
        elif user_1 == "5":
            main_windows()
            print("\n")
        elif user_1 == "6":
            main_linux()
            print("\n")
        elif user_1 == "9":
            main_both()
            print("\n")



if __name__ == '__main__':  # code to execute if called from command-line
    main()