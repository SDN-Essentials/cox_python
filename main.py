#!/usr/bin/env python


from net_device import EX
from net_device import SRX
import sys


def main():
    srx_1 = SRX('172.16.0.1', 'netconf', 'test123')
    srx_1.connect()
    print(srx_1.routes())
    ex_1 = EX('172.16.0.1', 'netconf', 'test123')
    ex_1.connect()
    print(ex_1.routes())
    if ex_1.routes() == srx_1.routes():
        print('Eeeexcellent.')

if __name__ == '__main__':
    sys.exit(main())
