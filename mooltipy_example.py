#!/usr/bin/env python
#
# Mooltipy development and example stub.

from mooltipy import *

import time


if __name__ == '__main__':

    logging.basicConfig(
            format='%(levelname)s\t %(funcName)s():\t %(message)s',
            level=logging.DEBUG)
            #level=logging.INFO)


    #hid_device, intf, epin, epout = findHIDDevice(USB_VID, USB_PID, True)
    mooltipass = Mooltipass()

    if mooltipass is None:
        sys.exit(0)

    if not mooltipass.ping():
        logging.error('Mooltipass did not reply to a ping request!')
        print('failure')
        sys.exit(0)


    while True:
        recv = mooltipass.get_status()
        if recv is None:
            print('error')
        else:
            if recv[DATA_INDEX] == 0:
                print('No card inserted')
            elif recv[DATA_INDEX] == 1:
                print('Mooltipass locked')
            elif recv[DATA_INDEX] == 3:
                print('Mooltipass locked, unlocking screen')
            elif recv[DATA_INDEX] == 5:
                print('Mooltipass unlocked')
            elif recv[DATA_INDEX] == 9:
                print('Unknown smart card')
            else:
                print('unknown resp: {0}'.format(str(recv[DATA_INDEX])))

        time.sleep(2)


    print('fin')
