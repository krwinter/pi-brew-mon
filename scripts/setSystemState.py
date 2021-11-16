#! /usr/bin/env python

import sys
import os
from subprocess import call, check_output
#import psutil
from getSystemState import get_system_state
#import ipdb

from config import vars as config
#from fermTempService import FermTempService

# TODO - write this as the fermTemp service

def set_system_state(mode):

	if int(mode) == 1:
		set_system_state_on()
	elif int(mode) == 0:
		set_system_state_off()
	elif int(mode) == -1:
		execute_restart()
	return mode


def set_system_state_on():

	print("Turning system on")
	if get_system_state() != 1:
		if config.ENV == 'pi' or os.path.isdir('/sys/bus/w1/devices/'):
			os.system('sudo service fermtemp start')

		#start run.py program
		#os.system("/home/ken/.virtualenvs/pi-mon/bin/python run.py")

		# do we want to make sure the service is running? and make sure it is?

		print("System turned on")
	else:
		print("--System was already on")



def set_system_state_off():
	print()"Starting to turn system off..."

	if get_system_state() == 1:
		# for proc in psutil.process_iter():
		#     try:
		#         pinfo = proc.as_dict(attrs=['pid', 'name', 'exe', 'cmdline'])
		#     except psutil.NoSuchProcess:
		#         pass
		#     else:
		#     	#processCommand = pinfo['cmdline']
		# 		#print (pinfo['cmdline'])
		# 		shell_command = pinfo['cmdline']
		# 		#print shell_command
		# 		if shell_command and 'python' in shell_command[0] and len(shell_command) > 0 and 'fermTempService.py' in shell_command[1]:
		# 			pid = pinfo['pid']
		# 			os.system('kill %d' % pid)
		# 			print "Killing PID {0}".format(pid)
		# 			break
		if config.ENV == 'pi' or os.path.isdir('/sys/bus/w1/devices/'):
			os.system('sudo service fermtemp stop')
			print("Killing Fermtemp Service")
	else:
		print("Nothing to kill here")


def execute_restart():

	set_system_state_off()

	# sleep for a sec

	set_system_state_on()



if __name__ == "__main__":
	print(set_system_state(sys.argv[1]))
