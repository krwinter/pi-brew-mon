#! /usr/bin/env python
import random
import os
import sys
from config import vars as config
from getRelayMode import get_relay_mode
import RPi.GPIO as GPIO

gpio_pin = 17


def hardware_on():
	if config.ENV == 'pi':
		os.system('sudo modprobe w1-gpio')
	    os.system('sudo modprobe w1-therm')
	    os.system('gpio -g mode 17 out')
	    os.system('gpio -g mode 22 out')

	    gpio_pin = 17
	    GPIO.setmode(GPIO.BCM)
	    GPIO.setup(gpio_pin, GPIO.OUT)
	print "Hardware turned on"


def hardware_off():
	# find process and kill
	running = 0

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
				os.system('kill %d' % pid
				print "Killing PID {0}".format(pid)
				break
				



def set_hardware_state(hardware_state):
    if hardware_state == 0 or hardware_state == 1
        print " --SET RELAY-- Turning hardware to state {0}".format(hardware_state)
        if hardware_state == 1:
        	hardware_on()
        else:
        	hardware_off()

    else:
        print "Invalid hardware_state, only 0 or 1 allowed"


if __name__ == "__main__":
	set_hardware_state(sys.argv[1])
    