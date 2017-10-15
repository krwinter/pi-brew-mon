#! /usr/bin/env python
import sys
import os

# env is passed in on command line - 'pi' or None currently
if len(sys.argv) > 1:
	env = sys.argv[1]
else:
	env = 'default'


MAIN_PY_FILE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
# these are typically relative to main py file
SET_TEMP_FILE_PATH = '/config/target_temp.txt'
RELAY_MODE_FILE_PATH = '/config/relay_mode.txt'	

MIN_SET_TEMP = 0
MAX_SET_TEMP = 40

UPPER_TEMP_SLOP = 0.5
LOWER_TEMP_SLOP = 0.5

if (env == 'pi' or os.path.isdir('/sys/bus/w1/devices/')):
	ENV = 'pi'
	TEMP_MODE = 'HEAT'
	GPIO_PIN = 17
	READ_TEMP_DIR = '/sys/devices/w1_bus_master1/28-00000520ce11'
	CURRENT_TEMP_CACHE = '/opt/fermtemp/config/currentTemp.txt'
elif (env == 'pi-cool'):
	ENV = 'pi-cool'
	TEMP_MODE = 'COOL'
	GPIO_PIN = 22
	READ_TEMP_DIR = '/sys/devices/w1_bus_master1/28-00000520ca72'
	CURRENT_TEMP_CACHE = '/opt/fermtemp/config/currentTemp.txt'
elif (env == 'local'):
	ENV = 'local'
	TEMP_MODE = 'HEAT'
	READ_TEMP_DIR = 'config/28-00000044ff99bb'
	CURRENT_TEMP_CACHE = 'config/currentTemp.txt'
else:
	ENV = 'node'
	TEMP_MODE = 'HEAT'
	READ_TEMP_DIR = 'python/config/28-00000044ff99bb'
	CURRENT_TEMP_CACHE = 'python/config/currentTemp.txt'

#print env
