#! /usr/bin/env python
import random
import os
import sys
from config import vars as config
from getRelayMode import get_relay_mode

gpio_pin = 17


relay_mode_file = os.path.join(os.path.dirname(sys.argv[0])) + '/config/relay_mode.txt'


def set_relay_mode(mode):
    # for now just a string in a file
    # allow: 'auto', 'on', or 'off'
    #print temp
    if mode == 'auto' or mode == 'on' or mode == 'off':
        f = open(relay_mode_file, 'w')
        f.write(mode)
        f.close()
        return True
    else:
        return False


if __name__ == "__main__":
	set_relay_mode(sys.argv[1])
	print str(get_relay_mode())