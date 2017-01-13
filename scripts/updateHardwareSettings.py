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

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
#base_dir = os.path.join(os.path.dirname(sys.argv[0]))
config_dir = base_dir   + '/config/'
data_dir = base_dir   + '/data/'
set_temp_file = config_dir + 'target_temp.txt'
poll_interval_file = config_dir + 'poll_interval.txt'
log_interval_file = config_dir + 'log_interval.txt'

# datafile_name = 'data/datafile' + str(time.strftime( "%Y%m%d_%H%M%S", time.localtime())) + '.csv'
# print "Creating datafile" + datafile_name

device_dir = '/sys/bus/w1/devices/'

logfilename='/var/log/fermtemp.log'

# how much we need to be away from set temp to take action
upper_temp_slop = 0.5
lower_temp_slop = 0.5

#logging
#logging.basicConfig(filename=logfilename,level=logging.INFO, format='%(asctime)s %(message)s')


# RUN

'''
- main update hardware from settings routine
'''


def set_relay_state_based_on_mode(relay_mode):

    if relay_mode == 'on':
        set_relay_state(1)
    elif relay_mode == 'off':
        set_relay_state(0)


# in this instance we're heating
def set_relay_state_based_on_temps():
    set_temp = get_set_temp()
    current_temp = get_current_temp()
    log_data("setTemp: {0}, currentTemp: {1}".format(set_temp, current_temp))
    desired_relay_state = 0

    if current_temp >= set_temp + upper_temp_slop:
        desired_relay_state = 0

    if current_temp <= set_temp - lower_temp_slop:
        desired_relay_state = 1

    relay_state = get_relay_state()
    if relay_state != desired_relay_state:
        relay_state = desired_relay_state
        set_relay_state(relay_state)
        log_info("*** Change relay to {0} ***".format(relay_state))



def log_info(message):
    # just print for now
    print message

def log_data(data):
    # just print for now
    log_info("*** " + data)

    #post to log server



def updateHardwareSettings():
    mode = get_relay_mode() # current temp, set temp, relay mode

    if mode == 'on' or mode == 'off':
        set_relay_state_based_on_mode(mode)
    elif mode == 'auto':
        set_relay_state_based_on_temps()
    # else shutdown???

if __name__ == "__main__":
    updateHardwareSettings()
