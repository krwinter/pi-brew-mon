#! /usr/bin/env python
import random
import os
import sys
from config import vars as config

gpio_pin = 17


relay_mode_file = os.path.join(os.path.dirname(sys.argv[0])) + '/config/relay_mode.txt'

def get_relay_mode():

	# for now just a string in a file
	f = open(relay_mode_file, 'r')
	relay_mode = f.readlines()
	f.close()

	return relay_mode[0]

#TODO - set so can use as cmd line or part of main daemon
if __name__ == "__main__":
    print str(get_relay_mode())