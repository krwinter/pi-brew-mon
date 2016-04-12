#! /usr/bin/env python

import sys
import os
from subprocess import call, check_output
from getSystemState import get_system_state

from config import vars as config



def set_system_state(mode):
	if mode == 1:
		set_system_state_on()
	elif mode == 0:
		set_system_state_off()
	elif mode == -1:
		execute_restart()
	return mode


def set_system_state_on():

	if config.ENV == 'pi' or os.path.isdir('/sys/bus/w1/devices/'):
		os.system('sudo modprobe w1-gpio')
		os.system('sudo modprobe w1-therm')
		os.system('gpio -g mode 17 out')
		os.system('gpio -g mode 22 out')

		gpio_pin = 17
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpio_pin, GPIO.OUT)

	if get_system_state() != 1:
		#start run.py program
		os.system("python run.py")

	
	print "System turned on"


def set_system_state_off():
	print "Starting to turn system off..."

	if get_system_state() == 1:
		for proc in psutil.process_iter():
		    try:
		        pinfo = proc.as_dict(attrs=['pid', 'name', 'exe', 'cmdline'])
		    except psutil.NoSuchProcess:
		        pass
		    else:
		    	#processCommand = pinfo['cmdline']
				#print (pinfo['cmdline'])
				shell_command = pinfo['cmdline']
				#print shell_command
				if shell_command and 'python' in shell_command[0] and len(shell_command) > 0 and 'run.py' in shell_command[1]:
					pid = pinfo['pid']
					os.system('kill %d' % pid)
					print "Killing PID {0}".format(pid)
					break
		# and maybe reset hardware?
	else:
		print "Nothing to kill here"


def execute_restart():

	set_system_state_off()

	set_system_state_on()



if __name__ == "__main__":
	print(set_system_state(sys.argv[1]))
