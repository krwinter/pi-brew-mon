#! /usr/bin/env python
import random
import os
import sys
from config import vars as config
from getRelayMode import get_relay_mode


gpio_pin = 17


def set_relay_state(relay_state):
    if int(relay_state) == 0 or int(relay_state) == 1:
        if os.path.isdir('/sys/bus/w1/devices/'):
            import RPi.GPIO as GPIO
            GPIO.output(gpio_pin, relay_state)
        print " --SET RELAY-- Setting GPIO to state {0}".format(relay_state)
    else:
        print "Invalid relay_state, only 0 or 1 allowed"


if __name__ == "__main__":
    set_relay_state(sys.argv[1])
