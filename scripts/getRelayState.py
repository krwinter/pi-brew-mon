#! /usr/bin/env python
import random
from config import vars as config

gpio_pin = 17


def get_relay_state():

	relay_state = 0
	if config.ENV == 'pi':
		import RPi.GPIO as GPIO
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpio_pin, GPIO.OUT)
		relay_state = GPIO.input(gpio_pin)
	else:
		relay_state = random.randint(0,1)

	return relay_state

#TODO - set so can use as cmd line or part of main daemon
print get_relay_state()