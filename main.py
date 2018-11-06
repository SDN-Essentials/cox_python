#!/usr/bin/env python


from EX import EX
from SRX import SRX
import sys


def main():
    srx_1 = SRX('172.16.0.1', 'netconf', 'test123')
    srx_1.connect()
    ex_1 = EX('172.16.0.1', 'netconf', 'test123')
    ex_1.connect()
    # Needs to print the message below.
    if ex_1.routes() == srx_1.routes():
        print('Eeeexcellent.')
    else:
        print('Please try again.')

if __name__ == '__main__':
    sys.exit(main())
