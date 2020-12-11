#!/usr/bin/env python
"""
Info about our project comes here
"""

from socket import *
import time

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

# This will scan all the ports for which ip-adress you put in
def main_poort():

    startTime = time.time()
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print('starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('port %d: OPEN' % (i,))
        s.close()

    print('Time taken', time.time() - startTime)

if __name__ == '__main__':
    main_poort()
