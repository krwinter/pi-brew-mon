#! /usr/bin/env python


import RPi.GPIO as GPIO

gpio_pin = 17

def get_relay_state():
    
    relay_state = 0

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.OUT)

    relay_state = GPIO.input(gpio_pin)

    return relay_state

#TODO - set so can use as cmd line or part of main daemon
print get_relay_state()