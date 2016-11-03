#! /usr/bin/env python
import sys
import os


# env is passed in on command line - 'pi' or None currently

if len(sys.argv) > 1:
	env = sys.argv[1]
else:
	env = 'default'

MIN_SET_TEMP = 5
MAX_SET_TEMP = 35

if (env == 'pi' or os.path.isdir('/sys/bus/w1/devices/')):
	MY_VAR = 'PI!!'
	ENV = 'pi'
	#READ_TEMP_DIR = '/sys/bus/w1/devices/'
	READ_TEMP_DIR = '/sys/devices/w1_bus_master1/28-00000520ce11'
	CURRENT_TEMP_CACHE = '/opt/fermtemp/scripts/config/currentTemp.txt'
elif (env == 'local'):
	MY_VAR = 'LOCAL'
	ENV = 'local'
	READ_TEMP_DIR = 'config/28-00000044ff99bb'
	CURRENT_TEMP_CACHE = 'config/currentTemp.txt'
else:
	MY_VAR = 'NODE'
	ENV = 'node'
	READ_TEMP_DIR = 'python/config/28-00000044ff99bb'
	CURRENT_TEMP_CACHE = 'python/config/currentTemp.txt'

#print env
