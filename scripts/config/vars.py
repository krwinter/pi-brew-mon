#! /usr/bin/env python
import sys


# env is passed in on command line - 'pi' or None currently

if len(sys.argv) > 1:
	env = sys.argv[1]
else:
	env = 'default'

MIN_SET_TEMP = 5
MAX_SET_TEMP = 35

if (env == 'pi'):
	MY_VAR = 'PI!!'
	ENV = 'pi'
	READ_TEMP_DIR = '/sys/bus/w1/devices/'
else:
	MY_VAR = 'NO PI'
	ENV = 'nopi'
	READ_TEMP_DIR = 'python/config/'

#print env