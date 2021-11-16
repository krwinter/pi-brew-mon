#!/home/ken/.virtualenvs/brewtemp/bin/python

#temp controller
import os
import sys
import glob
import time
import logging

from config import vars as config

from getSetTemp import get_set_temp
from getRelayMode import get_relay_mode
from getRelayState import get_relay_state
from getCurrentTemp import get_current_temp
from setRelayState import set_relay_state
from setSystemState import set_system_state
#import ipdb;ipdb.set_trace()


# how much we need to be away from set temp to take action
upper_temp_slop = 0.5
lower_temp_slop = 0.5


# RUN

'''
- main update hardware from settings routine
'''
def set_relay_state_based_on_mode(relay_mode):

    if relay_mode == 'on':
        set_relay_state(1)
    elif relay_mode == 'off':
        set_relay_state(0)


# heating vs cooling
def set_relay_state_based_on_temps():
    set_temp = get_set_temp()
    current_temp = get_current_temp()
    log_info("setTemp: {0}, currentTemp: {1}".format(set_temp, current_temp))
    desired_relay_state = 0

    # HERE'S where we do the opposite depending if we're heating or cooling
    # -- we are HEATING
    if (config.TEMP_MODE == 'HEAT'):
        if current_temp >= set_temp + config.UPPER_TEMP_SLOP:
            desired_relay_state = 0

        if current_temp <= set_temp - config.LOWER_TEMP_SLOP:
            desired_relay_state = 1
    # -- we are COOLING
    elif (config.TEMP_MODE == 'COOL'): 
        if current_temp >= set_temp + config.UPPER_TEMP_SLOP:
            desired_relay_state = 1

        if current_temp <= set_temp - config.LOWER_TEMP_SLOP:
            desired_relay_state = 0

    relay_state = get_relay_state()
    if relay_state != desired_relay_state:
        relay_state = desired_relay_state
        set_relay_state(relay_state)
        log_info("*** Change relay to {0} ***".format(relay_state))



def log_info(message):
    # just print for now
    if __name__ == "__main__":
        print(message)

def log_data(data):
    # just print for now
    log_info("*** " + data)



def updateHardwareSettings():
    mode = get_relay_mode() # current temp, set temp, relay mode

    if mode == 'on' or mode == 'off':
        set_relay_state_based_on_mode(mode)
    elif mode == 'auto':
        set_relay_state_based_on_temps()
    # else shutdown???

if __name__ == "__main__":
    updateHardwareSettings()
