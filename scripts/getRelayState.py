#! /usr/bin/env python
import random
import os

from config import vars as config


def get_relay_state():

	relay_state = 0
	if os.path.isdir('/sys/bus/w1/devices/'):
		import RPi.GPIO as GPIO
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(config.GPIO_PIN, GPIO.OUT)
		relay_state = GPIO.input(config.GPIO_PIN)
	else:
		relay_state = random.randint(0,1)

	return relay_state

if __name__ == "__main__":
	print(get_relay_state())