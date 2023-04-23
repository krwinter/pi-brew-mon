#! /usr/bin/env python
import sys
import os

# env is passed in on command line - 'pi' or None currently
# UPDATE - pi-cool and pi-heat
if len(sys.argv) > 1:
	env = sys.argv[1]
else:
	env = 'default'


#if (env == 'pi' or os.path.isdir('/sys/bus/w1/devices/')):

# figure out for relative paths
thisFilePath = os.path.abspath(__file__)
thisDirectory = os.path.dirname(thisFilePath)

if (env == 'pi' or env == 'pi-heat'):
	ENV = 'pi'
	DATA_FOLDER = '/data/channel1'
	TEMP_MODE = 'HEAT'
	LOWER_TEMP_SLOP = 0.5
	UPPER_TEMP_SLOP = 0.5
	GPIO_PIN = 17
	READ_TEMP_DIR = '/sys/devices/w1_bus_master1/28-00000520ce11'
	CURRENT_TEMP_CACHE = '/opt/fermtemp/config/channel1/currentTemp.txt'
elif (env == 'pi-cool'):
	ENV = 'pi-cool'
	DATA_FOLDER = '/data/channel2'
	TEMP_MODE = 'COOL'
	LOWER_TEMP_SLOP = -1
	UPPER_TEMP_SLOP = 1.5
	GPIO_PIN = 22
	READ_TEMP_DIR = '/sys/devices/w1_bus_master1/28-00000520ca72'
	CURRENT_TEMP_CACHE = '/opt/fermtemp/data/channel2/currentTemp.txt'
# heater and cooler together - heat channel 1, cool channel 2
elif (env == 'pi-heat-cooler'):
	ENV = 'pi-mix'
	# data - relay mode and target temp - are in channel 1
	DATA_FOLDER = '/data/channel1'
	TEMP_MODE = 'HEAT'
	LOWER_TEMP_SLOP = -1
	UPPER_TEMP_SLOP = 1.5
	# controls channel 1 - heat
	GPIO_PIN = 17
	# reads channel 2 temp
	READ_TEMP_DIR = '/sys/devices/w1_bus_master1/28-00000520ca72' 
	CURRENT_TEMP_CACHE = '/opt/fermtemp/data/channel2/currentTemp.txt'
elif (env == 'local'):
	ENV = 'local'
	DATA_FOLDER = '/data/local'
	TEMP_MODE = 'HEAT'
	LOWER_TEMP_SLOP = 0.5
	UPPER_TEMP_SLOP = 0.5
	READ_TEMP_DIR = os.path.join(thisDirectory, '28-00000044ff99bb')
	CURRENT_TEMP_CACHE = os.path.join(thisDirectory, 'currentTemp.txt')
elif (env == 'local1'):
	ENV = 'local1'
	DATA_FOLDER = '/data/local'
	TEMP_MODE = 'HEAT'
	LOWER_TEMP_SLOP = 0.5
	UPPER_TEMP_SLOP = 0.5
	READ_TEMP_DIR = os.path.join(thisDirectory, '28-00000044ff99bb')
	CURRENT_TEMP_CACHE = os.path.join(thisDirectory, 'currentTemp.txt')
elif (env == 'local2'):
	ENV = 'local2'
	DATA_FOLDER = '/data/local'
	TEMP_MODE = 'COOL'
	LOWER_TEMP_SLOP = 0.5
	UPPER_TEMP_SLOP = 0.5
	READ_TEMP_DIR = os.path.join(thisDirectory, '28-00')
	CURRENT_TEMP_CACHE = os.path.join(thisDirectory, 'currentTemp.txt')
else:
	ENV = 'node'
	DATA_FOLDER = '/data/local'
	TEMP_MODE = 'HEAT'
	READ_TEMP_DIR = 'config/28-0000'
	CURRENT_TEMP_CACHE = 'config/currentTemp.txt'


MAIN_PY_FILE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
# these are typically relative to main py file
SET_TEMP_FILE_PATH = DATA_FOLDER + '/target_temp.txt'
RELAY_MODE_FILE_PATH = DATA_FOLDER + '/relay_mode.txt'	

MIN_SET_TEMP = 0
MAX_SET_TEMP = 40

