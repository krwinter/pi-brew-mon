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
from updateHardwareSettings import updateHardwareSettings
#import ipdb;ipdb.set_trace()

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
config_dir = base_dir   + '/config/'
poll_interval_file = config_dir + 'poll_interval.txt'
log_interval_file = config_dir + 'log_interval.txt'


# RUN

'''
- make sure gpio is set up properly
- make sure we're using the right python env

START:
0. read polling interval / data record interval - loop accordingly
do while:
1. read relayMode - on, off, auto
    if on/off, make sure set
    else is auto
2. read set temp
3. relay on or off
4. record data if needed

'''

def startup():

    #set_system_state(1) # already done by service - we're running here aren't we
    setup_gpio()

    #get_polling_config()


def setup_gpio():
    if config.ENV == 'pi' or os.path.isdir('/sys/bus/w1/devices/'):
        import RPi.GPIO as GPIO
        os.system('sudo modprobe w1-gpio')
        os.system('sudo modprobe w1-therm')
        os.system('gpio -g mode 17 out')
        os.system('gpio -g mode 22 out')

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.GPIO_PIN, GPIO.OUT)
    log_info("GPIO hardware turned ON")


def get_polling_config():

    # for now just a string in a file
    f = open(poll_interval_file, 'r')
    poll_interval = f.readlines()[0]
    f.close()

    f = open(log_interval_file, 'r')
    log_interval = f.readlines()[0]
    f.close()

    log_info("Polling interval is {0} seconds".format(poll_interval))
    log_info("Logging interval is {0} seconds".format(log_interval))

    return int(poll_interval), int(log_interval)


def log_info(message):
    # just print for now
    print message

def log_data(data):
    # just print for now
    log_info("*** " + data)

    #post to log server


def main():

    startup()

    poll_interval, log_interval = get_polling_config()

    log_info("STARTING MAIN EVENT LOOP");

    loop_counter = 1
    while True:

        updateHardwareSettings()

        if log_interval%poll_interval == 0:
            #write_data()
            pass

        # # get and write the real temp from device (which is blocking) every 4 polls
        # # TODO - use a separate thread?
        # if loop_counter%4 == 0:
        #     print "Now we copy current temp from device"
        #     cache_current_temp();
        #     loop_counter = 1
        # else:
        #     loop_counter+=1

        time.sleep(int(poll_interval))


main()
